from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base


class BaseRepository:
    def __init__(self, session):
        self.session = session

    schema: type[BaseModel]
    model: type[Base]
    session: AsyncSession

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
