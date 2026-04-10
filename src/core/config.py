"""配置管理。"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Water Resource GIS"
    env: str = "development"
    api_prefix: str = "/api/v1"

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/water_resource_gis"
    redis_url: str = "redis://localhost:6379/0"

    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
