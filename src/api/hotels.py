from fastapi import APIRouter

from src.dependencies import DBDep
from src.schemas.hotels import HotelsPatch, HotelsPost, HotelsResponse
from src.schemas.responce import ApiResponse
from src.services.hotels import HotelsService

router = APIRouter()


@router.get("", response_model=ApiResponse[list[HotelsResponse]])
async def get_all(db: DBDep):
    hotel = await HotelsService(db).get_all()
    return ApiResponse(data=hotel)


@router.get("/{hotel_id}", response_model=ApiResponse[HotelsResponse])
async def get_one_or_none(db: DBDep, hotel_id: int):
    hotel = await HotelsService(db).get_one_or_none(hotel_id=hotel_id)
    return ApiResponse(data=hotel)


@router.post("", response_model=ApiResponse[HotelsResponse])
async def post(db: DBDep, data: HotelsPost):
    hotel = await HotelsService(db).post(data=data)
    return ApiResponse(data=hotel)


@router.put("/{hotel_id}", response_model=ApiResponse[HotelsResponse])
async def put(db: DBDep, data: HotelsPost, hotel_id: int):
    hotel = await HotelsService(db).put(data=data, hotel_id=hotel_id)
    return ApiResponse(data=hotel)


@router.patch("/{hotel_id}", response_model=ApiResponse[HotelsResponse])
async def patch(db: DBDep, data: HotelsPatch, hotel_id: int):
    hotel = await HotelsService(db).patch(data=data, hotel_id=hotel_id)
    return ApiResponse(data=hotel)


@router.delete("/{hotel_id}", response_model=ApiResponse[HotelsResponse])
async def delete(db: DBDep, hotel_id: int):
    hotel = await HotelsService(db).delete(hotel_id=hotel_id)
    return ApiResponse(data=hotel)
