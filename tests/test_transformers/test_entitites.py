from db2ndb.main import transform
from db2ndb.transformers import ReplaceKeyCall, ReplaceKeyNameKwarg


def test_replace_key_name_kwarg():
    before = """
MyModel(key_name='my_key')
"""

    after = """
MyModel(id='my_key')
"""

    transformers = [ReplaceKeyNameKwarg]

    assert transform(before, transformers) == after


def test_replace_key_call():
    before = """
model_instance.key()
"""

    after = """
model_instance.key
"""

    transformers = [ReplaceKeyCall]

    assert transform(before, transformers) == after
