from typing import Generic, TypeVar, Type, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")  # Criação do tipo genérico referente a entidade

# Classe do repository
class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model  # Entidade recebida
        self.db = db  # Conexão com database

    async def get_by_id(self, id: int) -> ModelType | None:
        # Select por id
        stmt = select(self.model).where(self.model.id == id)
        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()  # Serialização do retorno

    async def get_all(self) -> list[ModelType]:
        stmt = select(self.model)  # Select de tudo
        result = await self.db.execute(stmt)

        return list(result.scalars().all())  # Serialização de uma lista

    #                 tipificação de "atributo=valor"
    async def get_by(self, **filter: Any) -> list[ModelType]:
        # seleciona todos que tem um campo especifico igual a um atributo
        stmt = select(self.model).filter_by(**filter)
        result = await self.db.execute(stmt)

        return list(result.scalars().all())

    async def create(self, entity: ModelType) -> ModelType:
        self.db.add(entity)  # Add ao database
        await self.db.commit()  # Commita alterações
        await self.db.refresh(entity)  # Retorna classe atualizada por constraints

        return entity

    async def update(self, entity: ModelType, data: dict) -> ModelType:
        for fields, value in data.items():
            if hasattr(entity, fields) and fields != "id":
                setattr(entity, fields, value)

        await self.db.commit()
        await self.db.refresh(entity)

        return entity

    async def delete(self, entity: ModelType) -> str:
        await self.db.delete(entity)
        await self.db.commit()

        return "entity " + entity.__tablename__ + " has been successfully deleted"