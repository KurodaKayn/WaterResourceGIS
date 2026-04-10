"""初始化数据库结构。"""

from src.core.base import Base, engine
from src.modules.hydrology.models import WaterFeature  # noqa: F401
from src.modules.monitoring.models import MonitoringStation  # noqa: F401


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
