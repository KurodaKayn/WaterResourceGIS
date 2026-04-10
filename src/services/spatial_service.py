"""空间处理服务。"""

from shapely.geometry import shape
from shapely.ops import transform
import pyproj


class SpatialService:
    def create_buffer(self, geometry_geojson: dict, distance: float, unit: str = "meters") -> dict:
        geom = shape(geometry_geojson)

        if unit == "kilometers":
            distance = distance * 1000
        elif unit == "feet":
            distance = distance * 0.3048
        elif unit == "miles":
            distance = distance * 1609.344

        project_to_3857 = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True).transform
        project_to_4326 = pyproj.Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True).transform

        geom_3857 = transform(project_to_3857, geom)
        buffered_3857 = geom_3857.buffer(distance)
        buffered_4326 = transform(project_to_4326, buffered_3857)

        return buffered_4326.__geo_interface__
