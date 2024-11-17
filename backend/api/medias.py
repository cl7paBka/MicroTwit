from fastapi import APIRouter, Depends, status, UploadFile, File
from typing import Annotated, Dict
from backend.api.dependencies import get_api_key

router = APIRouter(
    prefix="/api/medias",
    tags=["Medias"]
)


@router.post("/api/medias")
async def upload_media(
    file: UploadFile = File(...),
    api_key: str = Depends(get_api_key)
):
    # Логика загрузки файла
    # Сохранение файла, генерация media_id и т.д.
    return {"result": True, "media_id": 1}


