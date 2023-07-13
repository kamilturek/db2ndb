from db2ndb.main import transform
from db2ndb.transformers import ReplaceBlobProperty


def test_replace_blob_property():
    before = """
db.BlobProperty()
"""

    after = """
ndb.BlobProperty()
"""

    transformers = [ReplaceBlobProperty]

    assert transform(before, transformers) == after