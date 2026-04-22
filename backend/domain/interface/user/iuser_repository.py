from abc import ABC, abstractmethod
from typing import Any

from domain.models.user import User
from schemas.dto.user_dto import LoginRequest

class IUserRepository(ABC):

    @abstractmethod
    async def get_by_id(self, id: int) -> User:
        ...

    @abstractmethod
    async def get_all(self) -> list[User]:
        ...

    @abstractmethod
    async def get_by(self, **filters: Any) -> list[User]:
        ...

    @abstractmethod
    async def create(self, entity: User) -> User:
        ...

    @abstractmethod
    async def update(self, entity: User, data: dict) -> User:
        ...

    @abstractmethod
    async def delete(self, entity: User) -> str:
        ...

    @abstractmethod
    async def get_by_username_and_password(self, request: LoginRequest) -> bool:
        ...