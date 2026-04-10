"""水利要素请求/响应模型。"""

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class WaterFeatureBase(BaseModel):
    name: str = Field(..., max_length=200)
    code: str = Field(..., max_length=50)
    feature_type: str = Field(...)
    metadata: dict[str, Any] | None = None


class WaterFeatureCreate(WaterFeatureBase):
    geometry: dict[str, Any] = Field(..., description="GeoJSON geometry")
    scale_level: int | None = None
    source_data: str | None = None


class WaterFeatureResponse(WaterFeatureBase):
    id: UUID
    geometry: dict[str, Any]
    geometry_type: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class PaginatedWaterFeatureResponse(BaseModel):
    items: list[WaterFeatureResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
