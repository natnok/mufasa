import json

from fastapi import APIRouter
from pydantic import BaseModel

from src import redis_manager
from src.dependencies import DBDep
from src.schemas.hotels import HotelsPatch, HotelsPost, HotelsResponse
from src.schemas.response import ApiResponse
from src.services.hotels import HotelsService
from src.tasks.tasks import task_1

router = APIRouter()


# @router.get("", response_model=ApiResponse[HotelsResponse])
# async def get_all(db: DBDep):
#     hotel = await HotelsService(db).get_all()
#     return ApiResponse(data=hotel)

# @router.get("", response_model=ApiResponse[HotelsResponse])
# async def get_all(db: DBDep):

#     hotels_from_cache = await redis_manager.get("hotels")
#     print("hotel from db")

#     if not hotels_from_cache:
#         hotel_from_db: list[BaseModel] = await HotelsService(db).get_all()
#         hotel_from_db_dicts = [model.model_dump() for model in hotel_from_db]
#         hotel_from_db_json = json.dumps(hotel_from_db_dicts)
#         hotels_to_redis = redis_manager.set("hotel_from_db_json", hotel_from_db_json)
#         print("hotel from cache")
#         return hotel_from_db

#     hotels_valid = json.loads(hotels_from_cache)
#     return hotels_valid


@router.get("")
async def get_all(db: DBDep):

    hotels_from_cache = await redis_manager.get("hotels")

    if not hotels_from_cache:
        hotel_from_db: list[BaseModel] = await HotelsService(db).get_all()
        hotel_from_db_dicts = [model.model_dump() for model in hotel_from_db]
        hotel_from_db_json = json.dumps(hotel_from_db_dicts)
        await redis_manager.set("hotels", hotel_from_db_json)
        print("bd")

        return hotel_from_db
    else:
        hotels_valid_cache = json.loads(hotels_from_cache)
        print("cache")
        task_1.delay()  # type: ignore
        return hotels_valid_cache


@router.get("/{hotel_id}", response_model=ApiResponse[HotelsResponse])
async def get_one_or_none(db: DBDep, hotel_id: int):
    hotel = await HotelsService(db).get_one_or_none(hotel_id=hotel_id)
    return ApiResponse(data=hotel)


@router.post("")
async def post(db: DBDep, data: HotelsPost):
    hotel = await HotelsService(db).post(data=data)
    return ApiResponse(data=hotel)


@router.put("/{hotel_id}")
async def put(db: DBDep, data: HotelsPost, hotel_id: int):
    hotel = await HotelsService(db).put(data=data, hotel_id=hotel_id)
    return ApiResponse(data=hotel)


@router.patch("/{hotel_id}")
async def patch(db: DBDep, data: HotelsPatch, hotel_id: int):
    hotel = await HotelsService(db).patch(data=data, hotel_id=hotel_id)
    return ApiResponse(data=hotel)


@router.delete("/{hotel_id}", response_model=ApiResponse[HotelsResponse])
async def delete(db: DBDep, hotel_id: int):
    hotel = await HotelsService(db).delete(hotel_id=hotel_id)
    return ApiResponse(data=hotel)
