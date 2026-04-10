"""监测站点与监测数据ORM模型。"""

import uuid
from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.core.base import Base


class MonitoringStation(Base):
    __tablename__ = "monitoring_stations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    station_code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    station_name: Mapped[str] = mapped_column(String(200), nullable=False)
    station_type: Mapped[str] = mapped_column(String(50), nullable=False)
    station_grade: Mapped[str | None] = mapped_column(String(10), nullable=True)
    location: Mapped[object] = mapped_column(Geometry("POINT", srid=4326), nullable=False)
    location_srid: Mapped[int] = mapped_column(nullable=False, default=4326)
    elevation: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    river_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("water_features.id"), nullable=True)
    basin_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    administrative_division: Mapped[str | None] = mapped_column(String(200), nullable=True)
    established_date: Mapped[datetime | None] = mapped_column(Date, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    __table_args__ = (
        CheckConstraint(
            "station_type IN ('rainfall', 'flow', 'water_level', 'water_quality', 'sediment')",
            name="chk_station_type",
        ),
    )
