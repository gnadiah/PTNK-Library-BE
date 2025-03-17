from typing import TypedDict

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import config
from app.auth.dto import UserRegisterRequest, UserLoginRequest
from app.database.models import User
from app.users.repository import UserRepository
from .utils import create_access_token, create_refresh_token, decode_refresh_token


class TokenResponse(TypedDict):
    access_token: str
    refresh_token: str
    token_type: str


class AuthService:
    @staticmethod
    async def register(db: AsyncSession, user_data: UserRegisterRequest) -> User:
        user = User(
            username=user_data.username,
            email=user_data.email.__str__(),
        )
        user.set_password(user_data.password)

        await UserRepository.create_user(db, user)
        return user

    @staticmethod
    async def login(db: AsyncSession, user_data: UserLoginRequest) -> TokenResponse:
        user = await UserRepository.get_user_by_username(db, user_data.username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not user.verify_password(user_data.password):
            raise HTTPException(status_code=400, detail="Incorrect password")

        return create_token(user)

    @staticmethod
    async def refresh_token(db: AsyncSession, refresh_token: str) -> TokenResponse:
        token_data = decode_refresh_token(refresh_token)
        if not token_data:
            raise HTTPException(status_code=400, detail="Invalid token")

        user = await UserRepository.get_user_by_id(db, token_data.get("id"))
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return create_token(user)


def create_token(user: User) -> TokenResponse:
    access_token = create_access_token({
        "sub": user.username,
        "id": user.id,
        "email": user.email,
        "is_admin": user.is_admin,
    })

    refresh_token = create_refresh_token({
        "sub": user.username,
        "id": user.id,
    })

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": config.JWT_TOKEN_TYPE,
    }
