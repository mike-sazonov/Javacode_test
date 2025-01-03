from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings
from app.db.database import Base

# TEST DB
engine_test = create_async_engine(settings.TEST_ASYNC_DATABASE_URl, poolclass=NullPool)
async_session_maker_test = async_sessionmaker(engine_test, class_=AsyncSession)


# drop test db
async def drop_test_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
