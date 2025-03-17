from pydantic import BaseModel, EmailStr, Field


class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=4, max_length=32, description="User name",
                          examples=["user", "user2"])
    email: EmailStr = Field(..., description="User email address",
                            examples=["user@example.com", "user2@example2.net"])
    password: str = Field(..., min_length=8, max_length=32, description="User password")
