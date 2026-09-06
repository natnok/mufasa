from src.schemas.rooms import RoomsPatch, RoomsPost
from src.services.base import BaseService


class RoomsService(BaseService):
    async def get_all(self):
        return await self.db.rooms.get_all()

    async def get_one_or_none(self, room_id: int):
        return await self.db.rooms.get_one_or_none(room_id=room_id)

    async def post(self, data: RoomsPost):
        room = await self.db.rooms.post(data=data)
        await self.db.commit()
        return room

    async def put(self, data: RoomsPost, room_id: int):
        room = await self.db.rooms.put(data=data, room_id=room_id)
        await self.db.commit()
        return room

    async def patch(self, data: RoomsPatch, room_id: int, exclude_unset: bool = True):
        room = await self.db.rooms.put(data=data, room_id=room_id, exclude_unset=exclude_unset)
        await self.db.commit()
        return room

    async def delete(self, room_id: int):
        room = await self.db.rooms.delete(room_id=room_id)
        await self.db.commit()
        return room
