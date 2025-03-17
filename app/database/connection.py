from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

import config

Base = declarative_base()

url = URL.create(
    drivername="mysql+asyncmy",
    username=config.DB_USER,
    password=config.DB_PASS,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
)

engine = create_async_engine(url)
AsyncDbSession = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
