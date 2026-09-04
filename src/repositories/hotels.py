from sqlalchemy.ext.asyncio import AsyncSession

from src.models.hotels import HotelsORM
from src.schemas.hotels import HotelsData


class HotelsRepository:
    schema: HotelsData
    model: HotelsORM
    session: AsyncSession
