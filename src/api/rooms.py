from fastapi import APIRouter

from src.dependencies import DBDep
from src.schemas.responce import ApiResponse
from src.schemas.rooms import RoomsPatch, RoomsPost, RoomsResponse
from src.services.rooms import RoomsService

router = APIRouter()


@router.get("", response_model=ApiResponse[list[RoomsResponse]])
async def get_all(db: DBDep):
    room = await RoomsService(db).get_all()
    return ApiResponse(data=room)


@router.get("/{room_id}", response_model=ApiResponse[RoomsResponse])
async def get_one_or_none(db: DBDep, room_id: int):
    room = await RoomsService(db).get_one_or_none(room_id=room_id)
    return ApiResponse(data=room)


@router.post("", response_model=ApiResponse[RoomsResponse])
async def post(db: DBDep, data: RoomsPost):
    room = await RoomsService(db).post(data=data)
    return ApiResponse(data=room)


@router.put("/{room_id}", response_model=ApiResponse[RoomsResponse])
async def put(db: DBDep, data: RoomsPost, room_id: int):
    room = await RoomsService(db).put(data=data, room_id=room_id)
    return ApiResponse(data=room)


@router.patch("/{room_id}", response_model=ApiResponse[RoomsResponse])
async def patch(db: DBDep, data: RoomsPatch, room_id: int):
    room = await RoomsService(db).patch(data=data, room_id=room_id)
    return ApiResponse(data=room)


@router.delete("/{room_id}", response_model=ApiResponse[RoomsResponse])
async def delete(db: DBDep, room_id: int):
    room = await RoomsService(db).delete(room_id=room_id)
    return ApiResponse(data=room)
