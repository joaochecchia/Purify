from typing import Generic, TypeVar
from pydantic import BaseModel
from datetime import datetime

ModelType = TypeVar("ModelType")

class BaseApiResponse(BaseModel, Generic[ModelType]):
    success: bool
    message: str
    data: ModelType | None = None
    status_code: int
    time_stamp: datetime

    @classmethod
    def success_response(
            cls,
            message: str,
            data: ModelType | None = None,
            status_code: int = 200
    ):
        return cls(
            success=True,
            message=message,
            data=data,
            status_code=status_code,
            time_stamp=datetime.now()
        )

    @classmethod
    def error_response(
            cls,
            message: str,
            status_code: int = 400,
            data: ModelType | None = None
    ):
        return cls(
            success=False,
            message=message,
            data=data,
            status_code=status_code,
            time_stamp=datetime.now()
        )