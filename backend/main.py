import os
import asyncio
import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.routers import all_routers
from backend.database.db import init_db
app = FastAPI()

for router in all_routers:
    app.include_router(router)

# Абсолютный путь к папке static, так как main.py находится не в корне проекта, а в папке backend
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")


async def main():
    await init_db()

    uvicorn.run('main:app', host='localhost', port=8000, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
