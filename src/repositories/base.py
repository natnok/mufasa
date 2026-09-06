from pydantic import BaseModel

from src.database import Base


class BaseRepository:
    model: type[Base]
    schema: type[BaseModel]

    def __init__(self, session):
        self.session = session

    async def get_all(self):
        pass

    async def get_one_or_none(self):
        pass

    async def post(self):
        pass

    async def put(self):
        pass

    async def patch(self):
        pass

    async def delete(self):
        pass
