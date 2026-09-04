from sqlalchemy.ext.asyncio import AsyncSession

from src.models.rooms import RoomsORM
from src.repositories.base import BaseRepository
from src.schemas.rooms import RoomsData


class RoomsRepository(BaseRepository):
    schema = RoomsData
    model = RoomsORM
    session: AsyncSession

