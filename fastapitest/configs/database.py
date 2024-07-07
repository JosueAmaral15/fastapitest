from typing import AsyncGenerator
import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapitest.configs.settings import settings

engine= create_async_engine(echo=False, url='postgresql+asyncpg://workout:workout@localhost:5432/workout')
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit = False
)

async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
