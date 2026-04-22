from domain.interface.user.iuser_service import IUserService
from infra.repositories.user_repository import UserRepository
from infra.mapper.user_mapper import UserMapper
from schemas.dto.user_dto import UserCreateRequest, UserUpdateRequest, UserResponse
from base_service import BaseService
from domain.models.user import User
from domain.interface.user.iuser_repository import IUserRepository
from domain.interface.user.iuser_service import IUserService

class UserService(
    BaseService[
        IUserRepository,
        UserCreateRequest,
        UserUpdateRequest,
        UserResponse,
        UserMapper,
        User
    ],
    IUserService
):
    def __init__(self, repository: IUserRepository, mapper: UserMapper):
        super().__init__(repository, mapper)

    async def register(self, entity: UserCreateRequest) -> UserResponse:
        model = self.mapper.create_request_to_model(entity)
        user = await self.repository.create(model)

        return self.mapper.model_to_response(user)
