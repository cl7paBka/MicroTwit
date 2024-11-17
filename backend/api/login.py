from fastapi import APIRouter, Depends, status, UploadFile, File
from typing import Annotated, Dict
from backend.api.dependencies import get_api_key

router = APIRouter()


@router.get("/login")
async def login(api_key: str = Depends(get_api_key)):
    return {"result": "True"}
