"""应用入口。"""

from fastapi import FastAPI

from src.api.middleware.error_handler import app_exception_handler
from src.api.routes import admin, analysis, monitoring, water_features
from src.core.config import settings
from src.core.exceptions import AppException

app = FastAPI(title=settings.app_name)
app.add_exception_handler(AppException, app_exception_handler)

app.include_router(water_features.router, prefix=settings.api_prefix)
app.include_router(monitoring.router, prefix=settings.api_prefix)
app.include_router(analysis.router, prefix=settings.api_prefix)
app.include_router(admin.router, prefix=settings.api_prefix)


@app.get("/health")
def health_check():
    return {"status": "ok"}
