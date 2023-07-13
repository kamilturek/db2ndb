# db2ndb

db2ndb tool is a Python CLI tool that helps you with migrating your App Engine
Python application from `google.appengine.ext.db` to `google.appengine.ext.ndb`
as per the official [DB to NDB Client Library Migration](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/db_to_ndb).

## Installation

```sh
pipx install db2ndb
```

## Usage

To convert the file, run:

```sh
db2ndb app.py
```

The output will be printed to the standard output. Use `-w` option to modify the
file in place.

```sh
db2ndb -w app.py
```

All transformations are enabled by default.
To disable a specific transformation, use the `--disable` option.

```sh
db2ndb --disable T001 app.py
```

## Supported Transformations

- `T001` - Replace `db.Model` base class with `ndb.Model`
- `T002` - Replace `kind` method definition with `_get_kind`
- `T003` - Replace `kind` method call with `_get_kind`
- `T004` - Replace `properties` method call with `_properties` attribute
- `T005` - Replace `dynamic_properties` method call with `_properties` attribute
- `T006` - Replace `key_name` keyword argument with `id`
- `T007` - Replace `key` method call with `key` attribute
- `T008` - Replace `db.BlobProperty()` with `ndb.BlobProperty()`

## License

This project is licensed under the terms of the [MIT license](./LICENSE).
