from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import AsyncDbSession


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncDbSession() as session:
        try:
            yield session
        finally:
            await session.close()


DatabaseDep = Annotated[AsyncSession, Depends(get_db)]
