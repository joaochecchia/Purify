from typing import Generic, TypeVar, Type, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.models.user import User

from domain.interface.user import iuser_repository
from schemas.dto.user_dto import LoginRequest
from base_repository import BaseRepository

class UserRepository(BaseRepository[User], iuser_repository):
    def __init__(self, db: AsyncSession):
        super().__init__(User, db)

    async def get_by_username_and_password(self, request: LoginRequest) -> bool:
        stmt = select(User).where(
            User.email == request.email,
            User.hash_password == request.password
        )

        result = await self.db.execute(stmt)
        user = result.scalar_one_or_none()

        return user is not None