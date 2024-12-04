from fastapi import APIRouter, Depends, status
from typing import Annotated, Dict


from backend.api.dependencies import get_api_key, tweets_service

from backend.services.tweets import TweetsService

from backend.schemas.tweets import CreateTweetSchema

router = APIRouter(
    prefix="/api/tweets",
    tags=["Tweets"]
)


@router.get("")
async def get_tweets(
        api_key: str = Depends(get_api_key)
):
    # Логика для возвращения списка твитов для текущего пользователя
    print(api_key)
    tweets = [
        {
            "id": 1,
            "content": "Hello World!",
            "attachments": ["link_1", "link_2"],
            "author": {"id": 1, "name": "User1"},
            "likes": [{"user_id": 2, "name": "User2"}]
        }
    ]
    return {"result": True, "tweets": tweets}


@router.post("")
async def create_tweet(
        tweet: CreateTweetSchema,
        service: Annotated[TweetsService, Depends(tweets_service)],
        api_key: str = Depends(get_api_key)  # Подключаем зависимость для API ключа
):
    # Логика создания твита
    # Валидация, сохранение в базу данных и т.д.
    created_tweet = await service.create_tweet(tweet)

    return {"result": True, "tweet_id": created_tweet.id}


@router.delete("/{tweet_id}")
async def delete_tweet(
        tweet_id: int,
        api_key: str = Depends(get_api_key)
):
    # Проверка, что пользователь может удалить этот твит
    # Логика удаления твита
    return {"result": True}


@router.post("/{tweet_id}/likes")
async def like_tweet(
        tweet_id: int,
        api_key: str = Depends(get_api_key)
):
    return {
        "result": True
    }


@router.delete("/{tweet_id}/likes")
async def unlike_tweet(
        tweet_id: int,
        api_key: str = Depends(get_api_key)
):
    return {
        "result": True
    }


