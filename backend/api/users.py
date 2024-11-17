from fastapi import APIRouter, Depends, status
from typing import Annotated, Dict
from backend.api.dependencies import get_api_key

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)


@router.post("/{user_id}/follow")
async def follow_user(
        user_id: int,
        api_key: str = Depends(get_api_key)
):
    return {
        "result": True
    }


@router.delete("/{user_id}/follow")
async def unfollow_user(
        user_id: int,
        api_key: str = Depends(get_api_key)
):
    return {
        "result": True
    }


@router.get("/me")
async def get_me(
        api_key: str = Depends(get_api_key)
):
    # Логика для возврата информации о текущем пользователе
    user_info = {
        "id": 1,
        "name": "User1",
        "followers": [{"id": 2, "name": "User2"}],
        "following": [{"id": 3, "name": "User3"}]
    }
    return {"result": "true", "user": user_info}


@router.get("/{user_id}")
async def get_user_info(
        user_id: int,
        api_key: str = Depends(get_api_key)
):
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
