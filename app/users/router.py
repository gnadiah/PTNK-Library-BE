from fastapi import APIRouter, Depends

from app.database.models import User
from app.dependencies.auth import get_current_user
from app.users.dto import MeResponse

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me", response_model=MeResponse)
async def me(
        user: User = Depends(get_current_user)
):
    return MeResponse.model_validate(user)
