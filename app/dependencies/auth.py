from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.utils import decode_access_token
from app.dependencies.database import get_db
from app.users.repository import UserRepository


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)

        token = creds.credentials

        token_data = decode_access_token(token)

        if not self.token_valid(token):
            raise HTTPException(status_code=401, detail="Invalid token")

        return token_data

    @staticmethod
    def token_valid(token: str) -> bool:
        token_data = decode_access_token(token)

        return token_data is not None


async def get_current_user(
        token_details: dict = Depends(TokenBearer()),
        db: AsyncSession = Depends(get_db),
):
    user_id = token_details.get("id")
    user = await UserRepository.get_user_by_id(db, user_id)
    return user
