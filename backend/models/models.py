from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY

from backend.database.db import Base
from backend.schemas.users import UserProfile, BasicUserInfo
from backend.schemas.tweets import TweetSchema, TweetLikeSchema

# Ассоциативная таблица для подписчиков и подписок
followers_table = Table(
    "followers",
    Base.metadata,
    Column("follower_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("following_id", Integer, ForeignKey("users.id"), primary_key=True)
)


class User(Base):
    """
    Таблица пользователей, содержит базовую информацию и связи с подписчиками.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # Связи: подписчики и подписки
    followers: Mapped[List["User"]] = relationship(
        "User",
        secondary=followers_table,
        primaryjoin=id == followers_table.c.following_id,
        secondaryjoin=id == followers_table.c.follower_id,
        backref="following"
    )

    # Явно обьявляю following, так как IDE не видит в строчке 47 self.following
    # following: Mapped[List["User"]]

    # Связь с твитами пользователя
    tweets: Mapped[List["Tweet"]] = relationship("Tweet", back_populates="author")

    def to_read_model(self) -> "UserProfile":
        """Преобразование в Pydantic схему UserProfile."""
        return UserProfile(
            id=self.id,
            name=self.name,
            followers=[BasicUserInfo(id=user.id, name=user.name) for user in self.followers],
            following=[BasicUserInfo(id=user.id, name=user.name) for user in self.following],
        )


class Tweet(Base):
    """
    Таблица твитов, содержит информацию о твитах и связь с авторами и лайками.
    """
    __tablename__ = "tweets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    attachments: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), nullable=True)

    # Автор твита
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["User"] = relationship("User", back_populates="tweets")

    # Связь с лайками
    likes: Mapped[List["TweetLike"]] = relationship("TweetLike", back_populates="tweet", cascade="all, delete-orphan")

    def to_read_model(self) -> "TweetSchema":
        """Преобразование в Pydantic схему Tweet."""
        return TweetSchema(
            id=self.id,
            content=self.content,
            attachments=self.attachments,
            author=self.author.to_read_model(),
            likes=[like.to_read_model() for like in self.likes] if self.likes else None
        )


class TweetLike(Base):
    """
    Таблица лайков для твитов.
    """
    __tablename__ = "tweet_likes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweets.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Связи
    tweet: Mapped["Tweet"] = relationship("Tweet", back_populates="likes")
    user: Mapped["User"] = relationship("User")

    def to_read_model(self) -> "TweetLikeSchema":
        """Преобразование в Pydantic схему TweetLike."""
        return TweetLikeSchema(
            tweet_id=self.tweet_id,
            user_id=self.user_id,
            name=self.user.name
        )
