from src.schemas.rooms import RoomsPatch, RoomsPost
from src.services.base import BaseService


class RoomsService(BaseService):
    async def get_all(self):
        return self.db.rooms.get_all()

    async def get_one_or_none(self, hotel_id: int):
        return self.db.rooms.get_one_or_none(hotel_id=hotel_id)

    async def post(self, data: RoomsPost):
        hotel = self.db.rooms.post(data=data)
        return hotel

    async def put(self, data: RoomsPost, hotel_id: int):
        hotel = self.db.rooms.put(data=data, hotel_id=hotel_id)
        return hotel

    async def patch(self, data: RoomsPatch, hotel_id: int, exclude_unset: bool = True):
        hotel = self.db.rooms.patch(data=data, exclude_unset=exclude_unset, hotel_id=hotel_id)
        return hotel

    async def delete(self, hotel_id: int):
        return self.db.rooms.delete(hotel_id=hotel_id)
