from src.services.spatial_service import SpatialService


def test_buffer_analysis_returns_polygon():
    service = SpatialService()
    point = {"type": "Point", "coordinates": [120.0, 30.0]}
    result = service.create_buffer(point, 1000, "meters")
    assert result["type"] in ["Polygon", "MultiPolygon"]
