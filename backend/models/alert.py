from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import String, DateTime, func, ForeignKey, Enum, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from configs.db import Base
from schemas.enums.risk_level import RiskLevel

if TYPE_CHECKING:
    from models.region import Region
    from models.water_quality_record import WaterQualityRecord


class Alert(Base):
    __tablename__ = "alert"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    alert_type: Mapped[str] = mapped_column(String(120), nullable=False)

    risk_level: Mapped[RiskLevel] = mapped_column(
        Enum(RiskLevel),
        nullable=False
    )

    message: Mapped[str] = mapped_column(Text, nullable=False)
    recommendation: Mapped[str | None] = mapped_column(Text, nullable=True)

    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    generated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    closed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    water_quality_record_id: Mapped[int] = mapped_column(
        ForeignKey("water_quality_record.id", ondelete="CASCADE"),
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

    water_quality_record: Mapped["WaterQualityRecord"] = relationship(
        back_populates="alerts"
    )

    region: Mapped["Region"] = relationship(
        back_populates="alerts"
    )