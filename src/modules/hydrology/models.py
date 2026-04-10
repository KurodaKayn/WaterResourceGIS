"""水利要素相关ORM模型。"""

import uuid
from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import Boolean, CheckConstraint, DateTime, Integer, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.core.base import Base


class WaterFeature(Base):
    __tablename__ = "water_features"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    feature_type: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    name_en: Mapped[str | None] = mapped_column(String(200), nullable=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    geometry: Mapped[object] = mapped_column(Geometry("GEOMETRY", srid=4326), nullable=False)
    geometry_type: Mapped[str] = mapped_column(String(20), nullable=False)
    geometry_srid: Mapped[int] = mapped_column(Integer, nullable=False, default=4326)
    source_data: Mapped[str | None] = mapped_column(String(100), nullable=True)
    scale_level: Mapped[int | None] = mapped_column(Integer, nullable=True)
    length_meters: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    area_sqm: Mapped[float | None] = mapped_column(Numeric(15, 2), nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSONB, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    created_by: Mapped[str | None] = mapped_column(String(100), nullable=True)
    updated_by: Mapped[str | None] = mapped_column(String(100), nullable=True)

    __table_args__ = (
        CheckConstraint("feature_type IN ('river', 'lake', 'reservoir', 'wetland', 'canal', 'dam')", name="chk_feature_type"),
        CheckConstraint(
            "geometry_type IN ('Point', 'LineString', 'Polygon', 'MultiPoint', 'MultiLineString', 'MultiPolygon')",
            name="chk_geometry_type",
        ),
    )
