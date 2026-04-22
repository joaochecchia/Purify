from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict

from schemas.enums.data_origin import DataOrigin
from schemas.enums.validation_status import ValidationStatus


class WaterQualityRecordCreateRequest(BaseModel):
    ph: Decimal
    turbidity: Decimal
    coliforms: Decimal
    collection_date: datetime
    data_origin: DataOrigin
    observation: str | None = None
    user_id: int
    region_id: int


class WaterQualityRecordUpdateRequest(BaseModel):
    ph: Decimal | None = None
    turbidity: Decimal | None = None
    coliforms: Decimal | None = None
    collection_date: datetime | None = None
    record_date: datetime | None = None
    data_origin: DataOrigin | None = None
    validation_status: ValidationStatus | None = None
    observation: str | None = None
    user_id: int | None = None
    region_id: int | None = None


class WaterQualityRecordResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ph: Decimal
    turbidity: Decimal
    coliforms: Decimal
    collection_date: datetime
    record_date: datetime
    data_origin: DataOrigin
    validation_status: ValidationStatus
    observation: str | None
    user_id: int
    region_id: int
    created_at: datetime
    updated_at: datetime