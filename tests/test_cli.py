import tempfile

from db2ndb import cli


def test_file_is_required(capsys):
    retcode = cli.run([])
    out, err = capsys.readouterr()

    assert retcode == 2
    assert out == ""
    assert "db2ndb: error: the following arguments are required: file" in err


def test_prints_transformed_file(capsys):
    with tempfile.NamedTemporaryFile("w") as fp:
        fp.write("db.BlobProperty()")
        fp.flush()

        retcode = cli.run([fp.name])
        out, err = capsys.readouterr()

        assert retcode == 0
        assert out == "ndb.BlobProperty()\n"
        assert err == ""


def test_writes_transformed_file(capsys):
    with tempfile.NamedTemporaryFile("r+") as fp:
        fp.write("db.BlobProperty()")
        fp.flush()

        retcode = cli.run(["-w", fp.name])
        out, err = capsys.readouterr()

        assert retcode == 0
        assert out == ""
        assert err == ""

        fp.seek(0)

        assert fp.read() == "ndb.BlobProperty()"
