from sqlalchemy.ext.asyncio import AsyncSession

from ..database.models import User


class UserRepository:
    @staticmethod
    async def create_user(db: AsyncSession, user: User) -> None:
        db.add(user)
        await db.commit()
        await db.refresh(user)

    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
        return await db.get(User, user_id)

    @staticmethod
    async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
        return await db.get(User, username == username)
