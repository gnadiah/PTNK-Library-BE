from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import DB_HOST, DB_USER, DB_PASS, DB_PORT, DB_NAME

Base = declarative_base()

url = URL.create(
    drivername="mysql+asyncmy",
    username=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

engine = create_async_engine(url)
AsyncDbSession = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
