from typing import Generic, TypeVar, Type, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.models.user import Users

from domain.interface.user.iuser_repository import IUserRepository
from schemas.dto.user_dto import LoginRequest
from infra.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[Users], IUserRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Users, db)

    async def get_by_username_and_password(self, request: LoginRequest) -> bool:
        stmt = select(Users).where(
            Users.email == request.email,
            Users.hash_password == request.password
        )

        result = await self.db.execute(stmt)
        user = result.scalar_one_or_none()

        return user is not None