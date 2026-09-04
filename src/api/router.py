from fastapi import APIRouter

from src.api import hotels, rooms

api_router_v1 = APIRouter(prefix="/api_v1")

api_router_v1.include_router(hotels.router, prefix="/hotels", tags=["hotel"])
api_router_v1.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
