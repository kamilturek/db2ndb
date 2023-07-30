# db2ndb

db2ndb tool is a Python CLI tool that helps you with migrating your App Engine
Python application from `google.appengine.ext.db` to `google.appengine.ext.ndb`
as per the official [DB to NDB Client Library Migration](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/db_to_ndb).

## Installation

Not released yet but you can still install the development version from GitHub.

```sh
git clone git@github.com:kamilturek/db2ndb.git
cd db2ndb
pip install .
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

### [Model class](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/db_to_ndb#model_class)

- `T001` - Replace `db.Model` base class with `ndb.Model`
- `T002` - Replace `kind` method definition with `_get_kind`
- `T003` - Replace `kind` method call with `_get_kind`
- `T004` - Replace `properties` method call with `_properties` attribute
- `T005` - Replace `dynamic_properties` method call with `_properties` attribute

### [Entities](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/db_to_ndb#entities)

- `T006` - Replace `key_name` keyword argument with `id`
- `T007` - Replace `key` method call with `key` attribute

### [Properties](https://cloud.google.com/appengine/docs/legacy/standard/python/ndb/db_to_ndb#properties)

- `T008` - Replace `db.BlobProperty()` with `ndb.BlobProperty()`
- `T009` - Replace `db.BooleanProperty()` with `ndb.BooleanProperty()`
- `T010` - Replace `db.ByteStringProperty()` with `ndb.BlobProperty(indexed=True)`
- `T011` - Replace `db.CategoryProperty()` with `ndb.StringProperty()`
- `T012` - Replace `db.DateProperty()` with `ndb.DateProperty()`
- `T013` - Replace `db.DateTimeProperty()` with `ndb.DateTimeProperty()`
- `T014` - Replace `db.EmailProperty()` with `ndb.StringProperty()`
- `T015` - Replace `db.FloatProperty()` with `ndb.FloatProperty()`
- `T016` - Replace `db.GeoPtProperty()` with `ndb.GeoPtProperty()`
- `T017` - Replace `db.IntegerProperty()` with `ndb.IntegerProperty()`
- `T018` - Replace `db.LinkProperty()` with `ndb.StringProperty()`
- `T019` - Replace `db.ListProperty(bool)` with `ndb.BooleanProperty(repeated=True)`
- `T020` - Replace `db.ListProperty(float)` with `ndb.FloatProperty(repeated=True)`
- `T021` - Replace `db.ListProperty(int)` with `ndb.IntegerProperty(repeated=True)`
- `T022` - Replace `db.ListProperty(db.Key)` with `ndb.KeyProperty(repeated=True)`
- `T023` - Replace `db.PhoneNumberProperty()` with `ndb.StringProperty()`
- `T024` - Replace `db.PostalAddressProperty()` with `ndb.StringProperty()`
- `T025` - Replace `db.RatingProperty()` with `ndb.IntegerProperty()`
- `T026` - Replace `db.ReferenceProperty(AnotherModel)` with `db.KeyProperty(kind=AnotherModel)`
- `T027` - Replace `db.SelfReferenceProperty()` with `ndb.KeyProperty(kind='ThisModelClass')`
- `T028` - Replace `db.StringProperty()` with `ndb.StringProperty()`
- `T029` - Remove `multiline` keyword argument from db.StringProperty()
- `T030` - Replace `db.StringListProperty()` with `ndb.StringProperty(repeated=True)`
- `T031` - Replace `db.TextProperty()` with `ndb.TextProperty()`
- `T032` - Replace `db.TimeProperty()` with `ndb.TimeProperty()`
- `T033` - Replace `db.UserProperty()` with `ndb.UserProperty()`
- `T034` - Replace `blobstore.BlobReferenceProperty()` with `ndb.BlobKeyProperty()`

## License

This project is licensed under the terms of the [MIT license](./LICENSE).
