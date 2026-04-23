from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from configs.db import Base

#Resolução de importação circular
if TYPE_CHECKING:
    from domain.models.user import Users
    from domain.models.region import Region

#inserção da dependência Base
class SanitationRecord(Base):
    __tablename__ = "sanitation_record"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    water_supply: Mapped[str] = mapped_column(String(120), nullable=False)
    sewage_collection: Mapped[str] = mapped_column(String(120), nullable=False)
    sewage_treatment: Mapped[str] = mapped_column(String(120), nullable=False)
    waste_collection: Mapped[str] = mapped_column(String(120), nullable=False)

    #Campo de FK
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), #Constraint FK
        nullable=False
    )

    region_id: Mapped[int] = mapped_column(
        ForeignKey("region.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    #Relacionamento
    region: Mapped["Region"] = relationship(
        back_populates="sanitation_records"
    )

    user: Mapped["Users"] = relationship(
        back_populates="sanitation_records"
    )