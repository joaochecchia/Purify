from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict

from schemas.enums.problem_type import ProblemType
from schemas.enums.occurrence_status import OccurrenceStatus


class SanitationOccurrenceCreateRequest(BaseModel):
    problem_type: ProblemType
    description: str
    latitude: Decimal
    longitude: Decimal
    user_id: int
    region_id: int


class SanitationOccurrenceUpdateRequest(BaseModel):
    problem_type: ProblemType | None = None
    description: str | None = None
    latitude: Decimal | None = None
    longitude: Decimal | None = None
    occurrence_status: OccurrenceStatus | None = None
    occurrence_date: datetime | None = None
    record_date: datetime | None = None
    user_id: int | None = None
    region_id: int | None = None


class SanitationOccurrenceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    problem_type: ProblemType
    description: str
    latitude: Decimal
    longitude: Decimal
    occurrence_status: OccurrenceStatus
    occurrence_date: datetime
    record_date: datetime
    user_id: int
    region_id: int
    created_at: datetime
    updated_at: datetime