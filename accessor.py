from typing import AsyncGenerator

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class PostgresAccessor:
    def __init__(self, db_url: str):
        self.engine = None
        self.async_session_maker = None
        self.db_url = db_url

    async def set_engine(self) -> None:
        self.engine = create_async_engine(
            url=self.db_url,
            echo=False,
            pool_pre_ping=True
        )

        self.async_session_maker = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )

    async def stop(self):
        await self.engine.dispose()

    @asynccontextmanager
    async def get_master_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker.begin() as session:
            yield session
