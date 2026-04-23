from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from configs.db import get_db
from infra.repositories.user_repository import UserRepository
from infra.mapper.user_mapper import UserMapper
from services.user_service import UserService

from domain.interface.user.iuser_service import IUserService


def get_user_service(
    db: AsyncSession = Depends(get_db)
) -> IUserService:
    repository = UserRepository(db)
    mapper = UserMapper()

    return UserService(repository, mapper)