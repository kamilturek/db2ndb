import pytest

from db2ndb.main import transform
from db2ndb.transformers import (
    RemoveMultilineKwarg,
    ReplaceBlobProperty,
    ReplaceBlobReferenceProperty,
    ReplaceBooleanProperty,
    ReplaceByteStringProperty,
    ReplaceCategoryProperty,
    ReplaceDateProperty,
    ReplaceDateTimeProperty,
    ReplaceEmailProperty,
    ReplaceFloatProperty,
    ReplaceGeoPtProperty,
    ReplaceIntegerProperty,
    ReplaceLinkProperty,
    ReplaceListPropertyBool,
    ReplaceListPropertyDBKey,
    ReplaceListPropertyFloat,
    ReplaceListPropertyInt,
    ReplacePhoneNumberProperty,
    ReplacePostalAddressProperty,
    ReplaceRatingProperty,
    ReplaceStringProperty,
    ReplaceTextProperty,
    ReplaceTimeProperty,
    ReplaceUserProperty,
    ReplaceReferenceProperty,
)


@pytest.mark.parametrize(
    "transformers,before,after",
    [
        ([ReplaceBlobProperty], "db.BlobProperty()", "ndb.BlobProperty()"),
        ([ReplaceBooleanProperty], "db.BooleanProperty()", "ndb.BooleanProperty()"),
        (
            [ReplaceByteStringProperty],
            "db.ByteStringProperty()",
            "ndb.BlobProperty(indexed=True)",
        ),
        ([ReplaceCategoryProperty], "db.CategoryProperty()", "ndb.StringProperty()"),
        ([ReplaceDateProperty], "db.DateProperty()", "ndb.DateProperty()"),
        ([ReplaceDateTimeProperty], "db.DateTimeProperty()", "ndb.DateTimeProperty()"),
        ([ReplaceEmailProperty], "db.EmailProperty()", "ndb.StringProperty()"),
        ([ReplaceFloatProperty], "db.FloatProperty()", "ndb.FloatProperty()"),
        ([ReplaceGeoPtProperty], "db.GeoPtProperty()", "ndb.GeoPtProperty()"),
        ([ReplaceIntegerProperty], "db.IntegerProperty()", "ndb.IntegerProperty()"),
        ([ReplaceLinkProperty], "db.LinkProperty()", "ndb.StringProperty()"),
        (
            [ReplaceListPropertyBool],
            "db.ListProperty(bool)",
            "ndb.BooleanProperty(repeated=True)",
        ),
        (
            [ReplaceListPropertyFloat],
            "db.ListProperty(float)",
            "ndb.FloatProperty(repeated=True)",
        ),
        (
            [ReplaceListPropertyInt],
            "db.ListProperty(int)",
            "ndb.IntegerProperty(repeated=True)",
        ),
        (
            [ReplaceListPropertyDBKey],
            "db.ListProperty(db.Key)",
            "ndb.KeyProperty(repeated=True)",
        ),
        (
            [ReplacePhoneNumberProperty],
            "db.PhoneNumberProperty()",
            "ndb.StringProperty()",
        ),
        (
            [ReplacePostalAddressProperty],
            "db.PostalAddressProperty()",
            "ndb.StringProperty()",
        ),
        ([ReplaceRatingProperty], "db.RatingProperty()", "ndb.IntegerProperty()"),
        (
            [ReplaceReferenceProperty],
            "db.ReferenceProperty(AnotherModel)",
            "ndb.KeyProperty(kind=AnotherModel)",
        ),
        ([ReplaceStringProperty], "db.StringProperty()", "ndb.StringProperty()"),
        (
            [ReplaceStringProperty, RemoveMultilineKwarg],
            "db.StringProperty(multiline=True)",
            "ndb.StringProperty()",
        ),
        ([ReplaceTextProperty], "db.TextProperty()", "ndb.TextProperty()"),
        ([ReplaceTimeProperty], "db.TimeProperty()", "ndb.TimeProperty()"),
        ([ReplaceUserProperty], "db.UserProperty()", "ndb.UserProperty()"),
        (
            [ReplaceBlobReferenceProperty],
            "blobstore.BlobReferenceProperty()",
            "ndb.BlobKeyProperty()",
        ),
    ],
)
def test_properties(transformers, before, after):
    assert transform(before, transformers) == after
