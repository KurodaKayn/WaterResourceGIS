"""校验工具。"""

from src.core.constants import ALLOWED_EPSG, FEATURE_TYPES, GEOMETRY_TYPES
from src.core.exceptions import ValidationException


def validate_epsg(epsg: int) -> None:
    if epsg not in ALLOWED_EPSG:
        raise ValidationException(f"不支持的EPSG: {epsg}")


def validate_feature_type(feature_type: str) -> None:
    if feature_type not in FEATURE_TYPES:
        raise ValidationException(f"不支持的要素类型: {feature_type}")


def validate_geometry_type(geometry_type: str) -> None:
    if geometry_type not in GEOMETRY_TYPES:
        raise ValidationException(f"不支持的几何类型: {geometry_type}")
