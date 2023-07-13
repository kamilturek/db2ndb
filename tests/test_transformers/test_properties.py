import pytest

from db2ndb.main import transform
from db2ndb.transformers import (
    ReplaceBlobProperty,
    ReplaceBlobReferenceProperty,
    ReplaceBooleanProperty,
    ReplaceCategoryProperty,
    ReplaceDateProperty,
    ReplaceDateTimeProperty,
    ReplaceEmailProperty,
    ReplaceFloatProperty,
    ReplaceGeoPtProperty,
    ReplaceIntegerProperty,
    ReplaceLinkProperty,
    ReplacePhoneNumberProperty,
    ReplacePostalAddressProperty,
    ReplaceRatingProperty,
    ReplaceStringProperty,
    ReplaceTextProperty,
    ReplaceTimeProperty,
    ReplaceUserProperty,
)


@pytest.mark.parametrize(
    "transformer,before,after",
    [
        (ReplaceBlobProperty, "db.BlobProperty()", "ndb.BlobProperty()"),
        (ReplaceBooleanProperty, "db.BooleanProperty()", "ndb.BooleanProperty()"),
        (ReplaceCategoryProperty, "db.CategoryProperty()", "ndb.StringProperty()"),
        (ReplaceDateProperty, "db.DateProperty()", "ndb.DateProperty()"),
        (ReplaceDateTimeProperty, "db.DateTimeProperty()", "ndb.DateTimeProperty()"),
        (ReplaceEmailProperty, "db.EmailProperty()", "ndb.StringProperty()"),
        (ReplaceFloatProperty, "db.FloatProperty()", "ndb.FloatProperty()"),
        (ReplaceGeoPtProperty, "db.GeoPtProperty()", "ndb.GeoPtProperty()"),
        (ReplaceIntegerProperty, "db.IntegerProperty()", "ndb.IntegerProperty()"),
        (ReplaceLinkProperty, "db.LinkProperty()", "ndb.StringProperty()"),
        (
            ReplacePhoneNumberProperty,
            "db.PhoneNumberProperty()",
            "ndb.StringProperty()",
        ),
        (
            ReplacePostalAddressProperty,
            "db.PostalAddressProperty()",
            "ndb.StringProperty()",
        ),
        (ReplaceRatingProperty, "db.RatingProperty()", "ndb.IntegerProperty()"),
        (ReplaceStringProperty, "db.StringProperty()", "ndb.StringProperty()"),
        (ReplaceTextProperty, "db.TextProperty()", "ndb.TextProperty()"),
        (ReplaceTimeProperty, "db.TimeProperty()", "ndb.TimeProperty()"),
        (ReplaceUserProperty, "db.UserProperty()", "ndb.UserProperty()"),
        (
            ReplaceBlobReferenceProperty,
            "blobstore.BlobReferenceProperty()",
            "ndb.BlobKeyProperty()",
        ),
    ],
)
def test_properties(transformer, before, after):
    assert transform(before, [transformer]) == after
