from src.utils.validators import validate_feature_type


def test_validate_feature_type_ok():
    validate_feature_type("river")
