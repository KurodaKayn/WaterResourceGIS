"""统一错误处理中间件。"""

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import Request
from fastapi.responses import JSONResponse

from src.core.exceptions import AppException


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": [],
                "request_id": str(uuid4()),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        },
    )
