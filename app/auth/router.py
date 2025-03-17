from typing import Annotated

from fastapi import APIRouter, Body

from app.auth.request_models import UserCreateRequest
from app.dependencies import DatabaseDep
from database.models import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register(
        user_data: Annotated[UserCreateRequest, Body(email=True)],
        db: DatabaseDep
):
    user = User(
        username=user_data.username,
        email=user_data.email.__str__(),
    )
    user.set_password(user_data.password)
    
    db.add(user)
    await db.commit()

    return {
        "message": "User created successfully",
        "user": user
    }


@router.get("/login")
async def login():
    return {"message": "Login"}
