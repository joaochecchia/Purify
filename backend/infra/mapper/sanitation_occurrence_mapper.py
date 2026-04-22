from domain.models.sanitation_occurrence import SanitationOccurrence
from schemas.dtos.sanitation_occurrence_dto import (
    SanitationOccurrenceCreateRequest,
    SanitationOccurrenceUpdateRequest,
    SanitationOccurrenceResponse,
)


class SanitationOccurrenceMapper:
    def create_request_to_model(
        self, request: SanitationOccurrenceCreateRequest
    ) -> SanitationOccurrence:
        return SanitationOccurrence(
            problem_type=request.problem_type,
            description=request.description,
            latitude=request.latitude,
            longitude=request.longitude,
            user_id=request.user_id,
            region_id=request.region_id,
        )

    def update_request_to_dict(
        self, request: SanitationOccurrenceUpdateRequest
    ) -> dict:
        return request.model_dump(exclude_none=True)

    def model_to_response(
        self, model: SanitationOccurrence
    ) -> SanitationOccurrenceResponse:
        return SanitationOccurrenceResponse.model_validate(model)