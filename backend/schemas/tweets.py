from typing import Optional, List
from pydantic import BaseModel
from backend.schemas.users import BasicUserInfo


class CreateTweetSchema(BaseModel):
    tweet_data: str
    tweet_media_ids: Optional[List[int]] = None


# Здесь наследуем BasicUserInfo, так как автор твита - пользователь
class TweetAuthor(BasicUserInfo):
    pass


class TweetLikeSchema(BaseModel):
    tweet_id: int
    user_id: int
    name: str


class TweetSchema(BaseModel):
    id: int
    content: str
    attachments: Optional[List[str]] = None  # Ссылки на media
    author: TweetAuthor
    likes: Optional[List[TweetLikeSchema]] = None
