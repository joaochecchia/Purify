from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

from schemas.enums.user_type import UserType


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    hash_password: str
    cpf_cnpj: str
    phone_number: str
    type: UserType


class UserUpdateRequest(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    hash_password: str | None = None
    cpf_cnpj: str | None = None
    phone_number: str | None = None
    type: UserType | None = None
    activate: bool | None = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    cpf_cnpj: str
    phone_number: str
    type: UserType
    activate: bool
    created_at: datetime
    updated_at: datetime

class LoginResponse(BaseModel):
    email: EmailStr