from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import DateTime, func, ForeignKey, Enum, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from configs.db import Base
from schemas.enums.data_origin import DataOrigin
from schemas.enums.validation_status import ValidationStatus

if TYPE_CHECKING:
    from domain.models.user import User
    from domain.models.region import Region
    from domain.models.alert import Alert


class WaterQualityRecord(Base):
    __tablename__ = "water_quality_record"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    ph: Mapped[float] = mapped_column(Numeric(4, 2), nullable=False)
    turbidity: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    coliforms: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    collection_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    record_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    data_origin: Mapped[DataOrigin] = mapped_column(
        Enum(DataOrigin),
        nullable=False
    )

    validation_status: Mapped[ValidationStatus] = mapped_column(
        Enum(ValidationStatus),
        nullable=False,
        default=ValidationStatus.PENDENTE
    )

    observation: Mapped[str | None] = mapped_column(Text, nullable=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
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

    user: Mapped["User"] = relationship(
        back_populates="water_quality_records"
    )

    region: Mapped["Region"] = relationship(
        back_populates="water_quality_records"
    )

    alerts: Mapped[list["Alert"]] = relationship(
        back_populates="water_quality_record",
        cascade="all, delete-orphan"
    )