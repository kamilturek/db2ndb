from db2ndb.transformations import TRANSFORMATIONS


def test_codes_are_unique():
    assert len(set(t.code for t in TRANSFORMATIONS)) == len(TRANSFORMATIONS)


def test_codes_are_sequential():
    codes = [int(t.code[1:]) for t in TRANSFORMATIONS]

    for code1, code2 in zip(codes, codes[1:]):
        assert code1 + 1 == code2
