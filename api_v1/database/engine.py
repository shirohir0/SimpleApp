from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import Depends

engine = create_async_engine('sqlite+aiosqlite:///api_v1/database/peoples.db')
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

session_depends = Annotated[AsyncSession, Depends(get_session)]