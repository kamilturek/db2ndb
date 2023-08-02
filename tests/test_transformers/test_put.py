from db2ndb.main import transform
from db2ndb.transformers import ReplaceDBPutCall


def test_replace_db_get_call_positional_key():
    before = "db.put(model_instance)"
    after = "model_instance.put()"

    transformers = [ReplaceDBPutCall]

    assert transform(before, transformers) == after


def test_replace_db_get_call_keyword_key():
    before = "db.put(models=model_instance)"
    after = "model_instance.put()"

    transformers = [ReplaceDBPutCall]

    assert transform(before, transformers) == after
