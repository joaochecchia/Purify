from abc import ABC, abstractmethod
from typing import Any

from schemas.dto.user_dto import UserCreateRequest, UserUpdateRequest, UserResponse, LoginRequest, LoginResponse

class IUserService:

    @abstractmethod
    async def get_by_id(self, id: int) -> UserResponse:
        ...

    @abstractmethod
    async def get_all(self) -> list[UserResponse]:
        ...

    @abstractmethod
    async def get_by(self, **filters: Any) -> list[UserResponse]:
        ...

    @abstractmethod
    async def register(self, entity: UserCreateRequest) -> UserResponse:
        ...

    @abstractmethod
    async def update(self, id: int, data: UserUpdateRequest) -> UserResponse:
        ...

    @abstractmethod
    async def delete(self, id: int) -> str:
        ...

    @abstractmethod
    async def get_by_username_and_password(self, request: LoginRequest) -> LoginResponse:
        ...