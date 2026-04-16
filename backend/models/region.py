from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import String, DateTime, func, Boolean, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from configs.db import Base

if TYPE_CHECKING:
    from models.sanitation_record import SanitationRecord
    from models.water_quality_record import WaterQualityRecord
    from models.alert import Alert
    from models.sanitation_occurrence import SanitationOccurrence


class Region(Base):
    __tablename__ = "region"

    __table_args__ = (
        UniqueConstraint("name", "state", "city"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    state: Mapped[str] = mapped_column(String(2), nullable=False)
    city: Mapped[str] = mapped_column(String(120), nullable=False)
    latitude: Mapped[float] = mapped_column(Numeric(10, 7), nullable=False)
    longitude: Mapped[float] = mapped_column(Numeric(10, 7), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

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
        back_populates="region",
        cascade="all, delete-orphan"
    )

    water_quality_records: Mapped[list["WaterQualityRecord"]] = relationship(
        back_populates="region",
        cascade="all, delete-orphan"
    )

    alerts: Mapped[list["Alert"]] = relationship(
        back_populates="region",
        cascade="all, delete-orphan"
    )

    sanitation_occurrences: Mapped[list["SanitationOccurrence"]] = relationship(
        back_populates="region",
        cascade="all, delete-orphan"
    )