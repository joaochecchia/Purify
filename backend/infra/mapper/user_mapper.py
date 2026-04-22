from domain.models.user import User
from schemas.dto.user_dto import (
    UserCreateRequest,
    UserUpdateRequest,
    UserResponse,
)


class UserMapper:
    def create_request_to_model(self, request: UserCreateRequest) -> User:
        return User(
            name=request.name,
            email=request.email,
            hash_password=request.hash_password,
            cpf_cnpj=request.cpf_cnpj,
            phone_number=request.phone_number,
            type=request.type,
        )

    def update_request_to_dict(self, request: UserUpdateRequest) -> dict:
        return request.model_dump(exclude_none=True)

    def model_to_response(self, model: User) -> UserResponse:
        return UserResponse.model_validate(model)