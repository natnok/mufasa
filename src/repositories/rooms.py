from sqlalchemy.ext.asyncio import AsyncSession

from src.models.rooms import RoomsORM
from src.schemas.rooms import RoomsData


class RoomsRepository:
    schema: RoomsData
    model: RoomsORM
    session: AsyncSession
