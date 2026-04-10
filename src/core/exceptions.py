"""自定义异常。"""


class AppException(Exception):
    """应用基础异常。"""

    def __init__(self, message: str, code: str = "APP_ERROR") -> None:
        self.message = message
        self.code = code
        super().__init__(message)


class ValidationException(AppException):
    """参数或数据验证异常。"""

    def __init__(self, message: str) -> None:
        super().__init__(message=message, code="VALIDATION_ERROR")


class NotFoundException(AppException):
    """资源不存在异常。"""

    def __init__(self, message: str) -> None:
        super().__init__(message=message, code="NOT_FOUND")


class UnauthorizedException(AppException):
    """认证或权限异常。"""

    def __init__(self, message: str = "未授权访问") -> None:
        super().__init__(message=message, code="UNAUTHORIZED")
