from src.utils.validators import validate_epsg


def test_validate_epsg_ok():
    validate_epsg(4326)
