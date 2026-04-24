from fastapi import APIRouter, Depends

from schemas.response.base_api_response import BaseApiResponse

from domain.interface.user.iuser_service import IUserService

from configs.dependencies import get_user_service

from schemas.dto.user_dto import (
    UserCreateRequest,
    UserUpdateRequest,
    UserResponse,
    LoginRequest
)

router = APIRouter(prefix="/user", tags=["Usuario"])


@router.post("/", response_model=BaseApiResponse)
async def create_user(
        request: UserCreateRequest,
        service: IUserService = Depends(get_user_service)
) -> BaseApiResponse[UserResponse]:
    new_user =  await service.register(request)

    response_entity = BaseApiResponse.success_response(
        f"User {request.name} successfully created.",
        new_user,
        201
    )

    return response_entity

@router.get("/{user_id}", response_model=BaseApiResponse)
async def get_user_by_id(
        user_id: int,
        service: IUserService = Depends(get_user_service)
) -> BaseApiResponse[UserResponse]:
    user = await service.get_by_id(user_id)

    response_entity = BaseApiResponse.success_response(
        f"User {user.name} successfully founded.",
        user,
        200
    )

    return response_entity

@router.get("/", response_model=BaseApiResponse)
async def get_all_users(
        service: IUserService = Depends(get_user_service)
) -> list[BaseApiResponse[UserResponse]]:
    user = await service.get_all()

    response_entity = BaseApiResponse.success_response(
        f"All users successfully founded.",
        user,
        200
    )

    return response_entity

@router.patch("/{user_id}", response_model=BaseApiResponse)
async def update_user(
        user_id: int,
        update_request: UserUpdateRequest,
        service: IUserService = Depends(get_user_service)
) -> BaseApiResponse[UserResponse]:
    updated_user = await service.update(user_id, update_request)

    response_entity = BaseApiResponse.success_response(
        f"All users successfully founded.",
        updated_user,
        200
    )

    return response_entity

@router.delete("/{user_id}", response_model=BaseApiResponse)
async def delete_user(
        user_id: int,
        service: IUserService = Depends(get_user_service)
) -> BaseApiResponse[str]:
    deletion_str = await service.delete(user_id)

    response_entity = BaseApiResponse.success_response(
        f"User successfully deleted.",
        deletion_str,
        204
    )

    return response_entity