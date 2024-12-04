from fastapi import Header, HTTPException, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.db import get_async_session


from backend.repositories.tweets import TweetsRepository
from backend.services.tweets import TweetsService


def get_api_key(api_key: str = Header(...)):
    # Поменять эту заглушку, когда сделаю бд
    valid_api_keys = ["test", "user", "admin"]
    if api_key not in valid_api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key


def tweets_service(session: AsyncSession = Depends(get_async_session)) -> TweetsService:
    tweets_repository = TweetsRepository(session=session)
    return TweetsService(tweets_repository)


