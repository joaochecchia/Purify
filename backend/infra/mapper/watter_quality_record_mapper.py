from domain.models.water_quality_record import WaterQualityRecord
from schemas.dto.water_quality_record_dto import (
    WaterQualityRecordCreateRequest,
    WaterQualityRecordUpdateRequest,
    WaterQualityRecordResponse,
)


class WaterQualityRecordMapper:
    def create_request_to_model(
        self, request: WaterQualityRecordCreateRequest
    ) -> WaterQualityRecord:
        return WaterQualityRecord(
            ph=request.ph,
            turbidity=request.turbidity,
            coliforms=request.coliforms,
            collection_date=request.collection_date,
            data_origin=request.data_origin,
            observation=request.observation,
            user_id=request.user_id,
            region_id=request.region_id,
        )

    def update_request_to_dict(
        self, request: WaterQualityRecordUpdateRequest
    ) -> dict:
        return request.model_dump(exclude_none=True)

    def model_to_response(
        self, model: WaterQualityRecord
    ) -> WaterQualityRecordResponse:
        return WaterQualityRecordResponse.model_validate(model)