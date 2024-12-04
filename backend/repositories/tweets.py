from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models.models import Tweet


class TweetsRepository:
    model = Tweet

    def __init__(self, session: AsyncSession):
        self.session = session


    async def create_tweet(self, data: dict):
        statement = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(statement)
        created_tweet = result.scalars().first()
        await self.session.commit()

        return created_tweet.to_read_model()
