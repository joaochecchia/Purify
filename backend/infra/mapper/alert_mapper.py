from domain.models.alert import Alert
from schemas.dto.alert_dto import (
    AlertCreateRequest,
    AlertUpdateRequest,
    AlertResponse,
)


class AlertMapper:
    def create_request_to_model(self, request: AlertCreateRequest) -> Alert:
        return Alert(
            alert_type=request.alert_type,
            risk_level=request.risk_level,
            message=request.message,
            recommendation=request.recommendation,
            water_quality_record_id=request.water_quality_record_id,
            region_id=request.region_id,
        )

    def update_request_to_dict(self, request: AlertUpdateRequest) -> dict:
        return request.model_dump(exclude_none=True)

    def model_to_response(self, model: Alert) -> AlertResponse:
        return AlertResponse.model_validate(model)