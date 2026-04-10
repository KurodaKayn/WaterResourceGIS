"""地理工具函数。"""

from shapely.geometry import shape

from src.core.exceptions import ValidationException


def validate_geometry(geometry: dict, expected_type: str | None = None) -> bool:
    geom = shape(geometry)
    if expected_type and geom.geom_type != expected_type:
        raise ValidationException(f"几何类型不匹配，期望 {expected_type}，实际 {geom.geom_type}")

    minx, miny, maxx, maxy = geom.bounds
    if minx < -180 or maxx > 180 or miny < -90 or maxy > 90:
        raise ValidationException("坐标超出WGS84范围")

    if not geom.is_valid:
        raise ValidationException("几何对象无效")

    return True
