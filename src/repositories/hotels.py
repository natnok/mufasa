from sqlalchemy.ext.asyncio import AsyncSession

from src.models.hotels import HotelsORM
from src.repositories.base import BaseRepository
from src.schemas.hotels import HotelsData


class HotelsRepository(BaseRepository):
    schema = HotelsData
    model = HotelsORM
    session: AsyncSession
