from fastapi import APIRouter, Depends, status
from typing import Annotated, Dict

router = APIRouter(
    prefix="/api/tweets",
    tags=["Tweets"]
)


@router.get("")
async def get_tweets():
    return {
        "tweets": [
            {"id": 1, "content": "Hello World!", "likes": 5},
            {"id": 2, "content": "FastAPI is awesome!", "likes": 15}
        ]
    }


@router.post("")
async def create_tweet():
    return {
        "result": True,
        "tweet_id": 1
    }


@router.delete("/{tweet_id}")
async def delete_tweet(tweet_id: int):
    return {
        "result": True
    }


@router.post("/{tweet_id}/likes")
async def like_tweet(tweet_id: int):
    return {
        "result": True
    }


@router.delete("/{tweet_id}/likes")
async def unlike_tweet(tweet_id: int):
    return {
        "result": True
    }
