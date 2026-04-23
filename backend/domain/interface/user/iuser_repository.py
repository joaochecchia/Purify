from abc import ABC, abstractmethod
from typing import Any

from domain.models.user import Users
from schemas.dto.user_dto import LoginRequest

class IUserRepository(ABC):

    @abstractmethod
    async def get_by_id(self, id: int) -> Users:
        ...

    @abstractmethod
    async def get_all(self) -> list[Users]:
        ...

    @abstractmethod
    async def get_by(self, **filters: Any) -> list[Users]:
        ...

    @abstractmethod
    async def create(self, entity: Users) -> Users:
        ...

    @abstractmethod
    async def update(self, entity: Users, data: dict) -> Users:
        ...

    @abstractmethod
    async def delete(self, entity: Users) -> str:
        ...

    @abstractmethod
    async def get_by_username_and_password(self, request: LoginRequest) -> bool:
        ...