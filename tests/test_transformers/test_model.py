from db2ndb.main import transform
from db2ndb.transformers import (
    ReplaceDBModelBase,
    ReplaceDynamicPropertiesCall,
    ReplaceKindCall,
    ReplaceKindDef,
    ReplacePropertiesCall,
)


def test_replace_db_model_base():
    before = """
class MyModel(db.Model):
    pass
"""

    after = """
class MyModel(ndb.Model):
    pass
"""

    transformers = [ReplaceDBModelBase]

    assert transform(before, transformers) == after


def test_replace_kind_def():
    before = """
@classmethod
def kind(cls):
    return 'Foo'
"""

    after = """
@classmethod
def _get_kind(cls):
    return 'Foo'
"""

    transformers = [ReplaceKindDef]

    assert transform(before, transformers) == after


def test_replace_kind_call():
    before = """
MyModel.kind()
"""

    after = """
MyModel._get_kind()
"""

    transformers = [ReplaceKindCall]

    assert transform(before, transformers) == after


def test_replace_properties_call():
    before = """
MyModel.properties()
"""

    after = """
MyModel._properties
"""

    transformers = [ReplacePropertiesCall]

    assert transform(before, transformers) == after


def test_replace_dynamic_properties_call():
    before = """
MyExpando.dynamic_properties()
"""

    after = """
MyExpando._properties
"""

    transformers = [ReplaceDynamicPropertiesCall]

    assert transform(before, transformers) == after
