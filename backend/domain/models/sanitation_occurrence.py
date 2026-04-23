from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import DateTime, func, ForeignKey, Enum, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from configs.db import Base
from schemas.enums.problem_type import ProblemType
from schemas.enums.occurrence_status import OccurrenceStatus

if TYPE_CHECKING:
    from domain.models.user import Users
    from domain.models.region import Region


class SanitationOccurrence(Base):
    __tablename__ = "sanitation_occurrence"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    problem_type: Mapped[ProblemType] = mapped_column(
        Enum(ProblemType),
        nullable=False
    )

    description: Mapped[str] = mapped_column(Text, nullable=False)

    latitude: Mapped[float] = mapped_column(Numeric(10, 7), nullable=False)
    longitude: Mapped[float] = mapped_column(Numeric(10, 7), nullable=False)

    occurrence_status: Mapped[OccurrenceStatus] = mapped_column(
        Enum(OccurrenceStatus),
        nullable=False,
        default=OccurrenceStatus.ABERTA
    )

    occurrence_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    record_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
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

    user: Mapped["Users"] = relationship(
        back_populates="sanitation_occurrences"
    )

    region: Mapped["Region"] = relationship(
        back_populates="sanitation_occurrences"
    )