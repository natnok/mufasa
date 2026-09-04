from src.schemas.hotels import HotelsPatch, HotelsPost
from src.services.base import BaseService


class HotelsService(BaseService):
    async def get_all(self):
        return self.db.hotels.get_all()

    async def get_one_or_none(self, hotel_id: int):
        return self.db.hotels.get_one_or_none(hotel_id=hotel_id)

    async def post(self, data: HotelsPost):
        hotel = self.db.hotels.post(data=data)
        return hotel

    async def put(self, data: HotelsPost, hotel_id: int):
        hotel = self.db.hotels.put(data=data, hotel_id=hotel_id)
        return hotel

    async def patch(self, data: HotelsPatch, hotel_id: int, exclude_unset: bool = True):
        hotel = self.db.hotels.patch(data=data, exclude_unset=exclude_unset, hotel_id=hotel_id)
        return hotel

    async def delete(self, hotel_id: int):
        return self.db.hotels.delete(hotel_id=hotel_id)
