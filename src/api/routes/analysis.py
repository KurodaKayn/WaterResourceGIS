"""空间分析API路由。"""

from fastapi import APIRouter

from src.api.schemas.analysis import BufferAnalysisRequest, BufferAnalysisResponse
from src.services.spatial_service import SpatialService
from src.utils.geo_utils import validate_geometry

router = APIRouter(prefix="/analysis", tags=["analysis"])


@router.post("/buffer", response_model=BufferAnalysisResponse)
def buffer_analysis(payload: BufferAnalysisRequest):
    validate_geometry(payload.geometry)
    spatial_service = SpatialService()
    result = spatial_service.create_buffer(payload.geometry, payload.distance, payload.unit)
    return {"result": result}
