from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from app.auth.dto import UserRegisterRequest, UserLoginResponse, UserLoginRequest, UserModel, UserRegisterResponse, \
    UserRefreshTokenResponse, UserRefreshTokenRequest
from app.auth.service import AuthService
from app.dependencies import DatabaseDep

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=UserRegisterResponse)
async def register(
        user_data: Annotated[UserRegisterRequest, Body()],
        db: DatabaseDep
):
    try:
        user = await AuthService.register(db, user_data)
        return {
            "message": "User created successfully",
            "user": UserModel.model_validate(user)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=UserLoginResponse)
async def login(
        user_data: Annotated[UserLoginRequest, Body()],
        db: DatabaseDep
):
    try:
        return await AuthService.login(db, user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/refresh-token", response_model=UserRefreshTokenResponse)
async def refresh_token(
        data: Annotated[UserRefreshTokenRequest, Body()],
        db: DatabaseDep
):
    try:
        return await AuthService.refresh_token(db, data.refresh_token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
