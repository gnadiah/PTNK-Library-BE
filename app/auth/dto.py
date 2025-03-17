from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=4, max_length=32, description="User name",
                          examples=["user", "user2"])
    email: EmailStr = Field(..., description="User email address",
                            examples=["user@example.com", "user2@example2.net"])
    password: str = Field(..., min_length=8, max_length=32, description="User password")


class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    username: str
    email: str
    created_at: datetime


class UserRegisterResponse(BaseModel):
    message: str
    user: UserModel


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
