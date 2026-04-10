"""水利要素数据访问层。"""

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.modules.hydrology.models import WaterFeature
from src.repositories.base_repository import BaseRepository


class WaterFeatureRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db)

    def list_paginated(self, page: int, page_size: int, feature_type: str | None = None):
        stmt = select(WaterFeature).where(WaterFeature.is_active.is_(True))
        count_stmt = select(func.count()).select_from(WaterFeature).where(WaterFeature.is_active.is_(True))

        if feature_type:
            stmt = stmt.where(WaterFeature.feature_type == feature_type)
            count_stmt = count_stmt.where(WaterFeature.feature_type == feature_type)

        total = self.db.execute(count_stmt).scalar_one()
        items = self.db.execute(stmt.offset((page - 1) * page_size).limit(page_size)).scalars().all()
        return items, total

    def get_by_id(self, feature_id):
        return self.db.get(WaterFeature, feature_id)
