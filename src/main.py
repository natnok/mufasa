import uvicorn
from fastapi import FastAPI

from src.api.router import api_router_v1
from src.config import settings

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
)

app.include_router(api_router_v1)

if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_reload,
    )
