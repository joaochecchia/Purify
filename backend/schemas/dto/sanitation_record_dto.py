from datetime import datetime
from pydantic import BaseModel, ConfigDict


class SanitationRecordCreateRequest(BaseModel):
    water_supply: str
    sewage_collection: str
    sewage_treatment: str
    waste_collection: str
    user_id: int
    region_id: int


class SanitationRecordUpdateRequest(BaseModel):
    water_supply: str | None = None
    sewage_collection: str | None = None
    sewage_treatment: str | None = None
    waste_collection: str | None = None
    user_id: int | None = None
    region_id: int | None = None


class SanitationRecordResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    water_supply: str
    sewage_collection: str
    sewage_treatment: str
    waste_collection: str
    user_id: int
    region_id: int
    created_at: datetime
    updated_at: datetime