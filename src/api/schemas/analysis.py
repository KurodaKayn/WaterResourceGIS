"""空间分析请求/响应模型。"""

from typing import Any, Literal

from pydantic import BaseModel, Field


class BufferAnalysisRequest(BaseModel):
    geometry: dict[str, Any] = Field(..., description="GeoJSON几何对象")
    distance: float = Field(..., gt=0, description="缓冲距离")
    unit: Literal["meters", "kilometers", "feet", "miles"] = "meters"


class BufferAnalysisResponse(BaseModel):
    result: dict[str, Any]
