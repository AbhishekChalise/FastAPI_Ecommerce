from typing import AsyncGenerator
from app.core.config import settings
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


engine = create_async_engine(
    url = settings.DATABASE_URL
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

class Base(DeclarativeBase):
    pass