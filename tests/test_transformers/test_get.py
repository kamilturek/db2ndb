from db2ndb.main import transform
from db2ndb.transformers import ReplaceDBGetCall, ReplaceGetByKeyNameCall


def test_replace_get_by_key_name_call():
    before = "MyModel.get_by_key_name('my_key')"
    after = "MyModel.get_by_id('my_key')"

    transformers = [ReplaceGetByKeyNameCall]

    assert transform(before, transformers) == after


def test_replace_db_get_call_positional_key():
    before = "db.get(key)"
    after = "key.get()"

    transformers = [ReplaceDBGetCall]

    assert transform(before, transformers) == after


def test_replace_db_get_call_keyword_key():
    before = "db.get(keys=key)"
    after = "key.get()"

    transformers = [ReplaceDBGetCall]

    assert transform(before, transformers) == after
