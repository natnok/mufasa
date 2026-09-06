from fastapi import APIRouter

from src.api import hotels, rooms

router_api_v1 = APIRouter(prefix="/api_v1")

router_api_v1.include_router(hotels.router, prefix="/hotels", tags=["hotels"])
router_api_v1.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
