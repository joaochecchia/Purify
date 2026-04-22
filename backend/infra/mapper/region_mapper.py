from domain.models.region import Region
from schemas.dto.region_dto import (
    RegionCreateRequest,
    RegionUpdateRequest,
    RegionResponse,
)


class RegionMapper:
    def create_request_to_model(self, request: RegionCreateRequest) -> Region:
        return Region(
            name=request.name,
            state=request.state,
            city=request.city,
            latitude=request.latitude,
            longitude=request.longitude,
        )

    def update_request_to_dict(self, request: RegionUpdateRequest) -> dict:
        return request.model_dump(exclude_none=True)

    def model_to_response(self, model: Region) -> RegionResponse:
        return RegionResponse.model_validate(model)