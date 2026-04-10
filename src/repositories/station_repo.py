"""监测站点数据访问层。"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.modules.monitoring.models import MonitoringStation
from src.repositories.base_repository import BaseRepository


class StationRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db)

    def list_active(self):
        stmt = select(MonitoringStation).where(MonitoringStation.is_active.is_(True))
        return self.db.execute(stmt).scalars().all()
