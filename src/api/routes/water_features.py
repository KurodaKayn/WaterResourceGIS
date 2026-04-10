"""水利要素API路由。"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.api.schemas.water_feature import PaginatedWaterFeatureResponse
from src.core.base import get_db
from src.core.constants import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from src.repositories.water_feature_repo import WaterFeatureRepository

router = APIRouter(prefix="/water-features", tags=["water-features"])


@router.get("", response_model=PaginatedWaterFeatureResponse)
def list_water_features(
    feature_type: str | None = Query(default=None),
    page: int = Query(default=DEFAULT_PAGE, ge=1),
    page_size: int = Query(default=DEFAULT_PAGE_SIZE, ge=1, le=100),
    db: Session = Depends(get_db),
):
    repo = WaterFeatureRepository(db)
    items, total = repo.list_paginated(page=page, page_size=page_size, feature_type=feature_type)
    total_pages = (total + page_size - 1) // page_size if total > 0 else 0

    return {
        "items": [],
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
    }
