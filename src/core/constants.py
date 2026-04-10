"""项目常量定义。"""

DEFAULT_CRS = 4326
ALLOWED_EPSG = [4326, 3857, 4490]

FEATURE_TYPES = ["river", "lake", "reservoir", "wetland", "canal", "dam"]
GEOMETRY_TYPES = [
    "Point",
    "LineString",
    "Polygon",
    "MultiPoint",
    "MultiLineString",
    "MultiPolygon",
]

API_V1_PREFIX = "/api/v1"
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
