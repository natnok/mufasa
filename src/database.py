from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import NullPool
from sqlalchemy.orm import DeclarativeBase

from src.config import settings
from sqlalchemy import


engine = create_async_engine(settings.DB_URL.unicode_string())
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

engine_null_pool = create_async_engine(settings.DB_URL.unicode_string(), pollclass=NullPool)
async_session_maker_null_pool = async_sessionmaker(engine_null_pool, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
