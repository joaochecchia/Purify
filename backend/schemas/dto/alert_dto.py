from datetime import datetime
from pydantic import BaseModel, ConfigDict

from schemas.enums.risk_level import RiskLevel


class AlertCreateRequest(BaseModel):
    alert_type: str
    risk_level: RiskLevel
    message: str
    recommendation: str | None = None
    water_quality_record_id: int
    region_id: int


class AlertUpdateRequest(BaseModel):
    alert_type: str | None = None
    risk_level: RiskLevel | None = None
    message: str | None = None
    recommendation: str | None = None
    active: bool | None = None
    closed_at: datetime | None = None
    water_quality_record_id: int | None = None
    region_id: int | None = None


class AlertResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    alert_type: str
    risk_level: RiskLevel
    message: str
    recommendation: str | None
    active: bool
    generated_at: datetime
    closed_at: datetime | None
    water_quality_record_id: int
    region_id: int
    created_at: datetime
    updated_at: datetime