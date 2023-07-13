from db2ndb.main import gather_transformers
from db2ndb.transformations import TRANSFORMATIONS


class TestGatherTransformers:
    def test_disabled_transformations_are_excluded(self):
        transformation = TRANSFORMATIONS[0]

        transformers = gather_transformers(transformation.code)

        assert transformation.transformer not in transformers
