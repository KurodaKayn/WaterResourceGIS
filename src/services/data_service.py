"""数据服务。"""

from src.repositories.water_feature_repo import WaterFeatureRepository


class DataService:
    def __init__(self, water_feature_repo: WaterFeatureRepository) -> None:
        self.water_feature_repo = water_feature_repo
