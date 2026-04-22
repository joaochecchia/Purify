from typing import Generic, TypeVar, Any

RepositoryType = TypeVar("RepositoryType")
CreateType = TypeVar("CreateType")
UpdateType = TypeVar("UpdateType")
ResponseType = TypeVar("ResponseType")
MapperType = TypeVar("MapperType")
ModelType = TypeVar("ModelType")


class BaseService(
    Generic[
        RepositoryType,
        CreateType,
        UpdateType,
        ResponseType,
        MapperType,
        ModelType
    ]
):
    def __init__(self, repository: RepositoryType, mapper: MapperType):
        self.repository = repository
        self.mapper = mapper

    async def get_by_id(self, id: int) -> ResponseType | None:
        res = await self.repository.get_by_id(id)

        if res is None:
            return None

        return self.mapper.model_to_response(res)

    async def get_all(self) -> list[ResponseType]:
        res = await self.repository.get_all()

        return [self.mapper.model_to_response(model) for model in res]

    async def get_by(self, **filters: Any) -> list[ResponseType]:
        res = await self.repository.get_by(**filters)

        return [self.mapper.model_to_response(model) for model in res]

    async def create(self, dto: CreateType) -> ResponseType:
        model = self.mapper.create_request_to_model(dto)
        res = await self.repository.create(model)

        return self.mapper.model_to_response(res)

    async def update(self, id: int, alter: UpdateType) -> ResponseType | None:
        entity = await self.repository.get_by_id(id)
        if entity is None:
            return None

        data = self.mapper.update_request_to_dict(alter)
        res = await self.repository.update(entity, data)

        return self.mapper.model_to_response(res)

    async def delete(self, id: int) -> str | None:
        entity = await self.repository.get_by_id(id)
        if entity is None:
            return None

        return await self.repository.delete(entity)