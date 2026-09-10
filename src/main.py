from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src import redis_manager
from src.api.router import router_api_v1
from src.config import settings
from src.tasks.tasks import task_2


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_manager.connect()
    yield
    await redis_manager.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.app_title,
    version=settings.app_version,
)


app.include_router(router_api_v1)

task_2.delay()  # type:ignore

if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_reload,
    )

!!!_fix_!!!