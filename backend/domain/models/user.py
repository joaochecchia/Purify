from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import String, UniqueConstraint, Enum, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from configs.db import Base
from schemas.enums.user_type import UserType

if TYPE_CHECKING:
    from domain.models.sanitation_record import SanitationRecord
    from domain.models.water_quality_record import WaterQualityRecord
    from domain.models.sanitation_occurrence import SanitationOccurrence


class Users(Base):
    __tablename__ = "users"

    __table_args__ = (
        UniqueConstraint("email"),
        UniqueConstraint("cpf_cnpj"),
        UniqueConstraint("phone_number"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    hash_password: Mapped[str] = mapped_column(String(255), nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(String(20), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    type: Mapped[UserType] = mapped_column(Enum(UserType), nullable=False)
    activate: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

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

    sanitation_records: Mapped[list["SanitationRecord"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    water_quality_records: Mapped[list["WaterQualityRecord"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    sanitation_occurrences: Mapped[list["SanitationOccurrence"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )