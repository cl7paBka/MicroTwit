from fastapi import APIRouter, Depends, status
from typing import Annotated, Dict

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)


@router.post("/{user_id}/follow")
async def follow_user(user_id: int):
    return {
        "result": True
    }


@router.delete("/{user_id}/follow")
async def unfollow_user(user_id: int):
    return {
        "result": True
    }


@router.get("/me")
async def get_me():
    return {
        "result": "true",
        "user": {
            "id": "123",
            "name": "str",
            "followers": [
                {
                    "id": "612",
                    "name": "str"
                }
            ],
            "following": [
                {
                    "id": "734",
                    "name": "str"
                }
            ]
        }
    }


@router.get("/{user_id}")
async def get_user_info(user_id: int):
    return {
        "result": "true",
        "user": {
            "id": "int",
            "name": "str",
            "followers": [
                {
                    "id": "int",
                    "name": "str"
                }
            ],
            "following": [
                {
                    "id": "int",
                    "name": "str"
                }
            ]
        }
    }
