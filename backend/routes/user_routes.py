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
):
    response =  await service.register(request)

    response_entity = BaseApiResponse.success_response(
        f"User {request.name} successfully created.",
        response,
        201
    )

    return response_entity