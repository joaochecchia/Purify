from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class RegionCreateRequest(BaseModel):
    name: str
    state: str
    city: str
    latitude: Decimal
    longitude: Decimal


class RegionUpdateRequest(BaseModel):
    name: str | None = None
    state: str | None = None
    city: str | None = None
    latitude: Decimal | None = None
    longitude: Decimal | None = None
    active: bool | None = None


class RegionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    state: str
    city: str
    latitude: Decimal
    longitude: Decimal
    active: bool
    created_at: datetime
    updated_at: datetime