from typing import Generator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


Base = declarative_base()
DATABASE_URL = f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

# DATABASE_URL = "mysql+asyncmy://scaner_user:scaner_user1@localhost:3306/scaner_db"
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session =sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session : AsyncSession = async_session()
        yield session
    finally:
        await session.close()
