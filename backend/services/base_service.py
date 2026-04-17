from typing import Generic, TypeVar, Any

RepositoryType = TypeVar("RepositoryType")
DtoType = TypeVar("DtoType")
MapperType = TypeVar("MapperType")
ModelType = TypeVar("ModelType")

class BaseService(Generic[RepositoryType, DtoType, MapperType, ModelType]):
    def __init__(self, repository: RepositoryType, mapper: MapperType):
        self.repository = repository
        self.mapper = mapper

    async def get_by_id(self, id: int) -> DtoType | None:
        res = await self.repository.get_by_id(id)

        if res is None:
            return None

        return self.mapper.model_to_dto(res)

    async def get_all(self) -> list[DtoType]:
        res = await self.repository.get_all()

        return [self.mapper.model_to_dto(model) for model in res]

    async def get_by(self, **filter: Any) -> list[DtoType]:
        res = await self.repository.get_by(**filter)

        return [self.mapper.model_to_dto(model) for model in res]

    async def create(self, dto: DtoType) -> DtoType:
        model = self.mapper.dto_to_model(dto)
        res = await self.repository.create(model)

        return self.mapper.model_to_dto(res)

    async def update(self, id: int, alter: DtoType) -> DtoType | None:
        entity = await self.repository.get_by_id(id)
        if entity is None:
            return None

        data = self.mapper.dto_to_dict(alter)
        res = await self.repository.update(entity, data)

        return self.mapper.model_to_dto(res)

    async def delete(self, id: int) -> str | None:
        entity = await self.repository.get_by_id(id)
        if entity is None:
            return None

        return await self.repository.delete(entity)