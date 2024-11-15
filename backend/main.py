import os
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from backend.api.routers import all_routers

app = FastAPI()

# Абсолютный путь к папке static, так как main.py находится не в корне проекта, а в папке backend
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html") as f:
        return f.read()


# Include all routers from the API package
for router in all_routers:
    app.include_router(router)


async def main():
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
