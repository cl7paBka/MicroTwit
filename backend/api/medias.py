from fastapi import APIRouter, Depends, status
from typing import Annotated, Dict

router = APIRouter(
    prefix="/api/tweets",
    tags=["Tweets"]
)


@router.post("")
async def upload_media():
    return {
        "result": True,
        "media_id": 1
    }


