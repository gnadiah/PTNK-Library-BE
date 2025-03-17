from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from app.auth.dto import UserRegisterRequest, UserLoginResponse, UserLoginRequest, UserModel, UserRegisterResponse
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
        data = await AuthService.login(db, user_data)
        return {
            "access_token": data.get("access_token"),
            "refresh_token": data.get("refresh_token"),
            "token_type": data.get("token_type")
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
