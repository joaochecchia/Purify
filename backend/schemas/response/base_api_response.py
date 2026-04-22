from typing import Generic, TypeVar
from datetime import datetime

ModelType = TypeVar("ModelType")

class BaseApiResponse(Generic[ModelType]):
    def __init__(
        self,
        success: bool | None = None,
        message: str | None = None,
        data: ModelType | None = None,
        status_code: int | None = None
    ):
        self.success = success
        self.message = message
        self.data = data
        self.status_code = status_code
        self.time_stamp = datetime.now()

    @classmethod
    def success(cls, message: str, data: ModelType | None = None, status_code: int = 200):
        return cls(True, message, data, status_code)

    @classmethod
    def error(cls, message: str, status_code: int = 400, data: ModelType | None = None):
        return cls(False, message, data, status_code)