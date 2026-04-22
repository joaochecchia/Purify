from domain.models.sanitation_record import SanitationRecord
from schemas.dto.sanitation_record_dto import (
    SanitationRecordCreateRequest,
    SanitationRecordUpdateRequest,
    SanitationRecordResponse,
)


class SanitationRecordMapper:
    def create_request_to_model(
        self, request: SanitationRecordCreateRequest
    ) -> SanitationRecord:
        return SanitationRecord(
            water_supply=request.water_supply,
            sewage_collection=request.sewage_collection,
            sewage_treatment=request.sewage_treatment,
            waste_collection=request.waste_collection,
            user_id=request.user_id,
            region_id=request.region_id,
        )

    def update_request_to_dict(
        self, request: SanitationRecordUpdateRequest
    ) -> dict:
        return request.model_dump(exclude_none=True)

    def model_to_response(self, model: SanitationRecord) -> SanitationRecordResponse:
        return SanitationRecordResponse.model_validate(model)