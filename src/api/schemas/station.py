"""监测站点请求/响应模型。"""

from pydantic import BaseModel, Field


class StationResponse(BaseModel):
    station_code: str = Field(..., max_length=50)
    station_name: str = Field(..., max_length=200)
    station_type: str

    model_config = {"from_attributes": True}
