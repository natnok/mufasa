from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base


class BaseRepository:
    def __init__(self, session):
        self.session = session

    schema: type[BaseModel]
    model: type[Base]
    session: AsyncSession

    async def get_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"kiteral_binds": True}))
        return [self.schema.model_validate(model) for model in result.scalars().all()]

    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"kiteral_binds": True}))
        model = result.scalars().one_or_none()
        return self.schema.model_validate(model)

    async def post(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        print(stmt.compile(compile_kwargs={"kiteral_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model)

    async def put(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        stmt = (
            update(self.model)
            .filter_by(**filter_by)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        print(stmt.compile(compile_kwargs={"kiteral_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model)

    async def patch(self, data: BaseModel, exclude_unset: bool = True, **filter_by):
        stmt = (
            update(self.model)
            .filter_by(**filter_by)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        print(stmt.compile(compile_kwargs={"kiteral_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model)

    async def delete(self, **filter_by):
        query = delete(self.model).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(query)
        print(query.compile(compile_kwargs={"kiteral_binds": True}))
        model = result.scalars().one()
        return self.schema.model_validate(model)
