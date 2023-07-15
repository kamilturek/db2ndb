from dataclasses import dataclass
from typing import Optional

from db2ndb.transformers import (
    ReplaceBlobProperty,
    ReplaceBooleanProperty,
    ReplaceByteStringProperty,
    ReplaceCategoryProperty,
    ReplaceDateProperty,
    ReplaceDateTimeProperty,
    ReplaceDBModelBase,
    ReplaceDynamicPropertiesCall,
    ReplaceEmailProperty,
    ReplaceFloatProperty,
    ReplaceGeoPtProperty,
    ReplaceIntegerProperty,
    ReplaceKeyCall,
    ReplaceKeyNameKwarg,
    ReplaceKindCall,
    ReplaceKindDef,
    ReplaceLinkProperty,
    ReplaceListPropertyBool,
    ReplaceListPropertyDBKey,
    ReplaceListPropertyFloat,
    ReplaceListPropertyInt,
    ReplacePhoneNumberProperty,
    ReplacePostalAddressProperty,
    ReplacePropertiesCall,
    ReplaceRatingProperty,
    ReplaceReferenceProperty,
)
from db2ndb.typing import TransformerType

__all__ = ("TRANSFORMATIONS",)


@dataclass
class Transformation:
    code: str
    description: Optional[str]
    transformer: TransformerType


TRANSFORMATIONS = (
    Transformation(
        code="T001",
        description="Replace `db.Model` base class with `ndb.Model`",
        transformer=ReplaceDBModelBase,
    ),
    Transformation(
        code="T002",
        description="Replace `kind` method definition with `_get_kind`",
        transformer=ReplaceKindDef,
    ),
    Transformation(
        code="T003",
        description="Replace `kind` method call with `_get_kind`",
        transformer=ReplaceKindCall,
    ),
    Transformation(
        code="T004",
        description="Replace `properties` method call with `_properties` attribute",
        transformer=ReplacePropertiesCall,
    ),
    Transformation(
        code="T005",
        description=(
            "Replace `dynamic_properties` method call with `_properties` attribute"
        ),
        transformer=ReplaceDynamicPropertiesCall,
    ),
    Transformation(
        code="T006",
        description="Replace `key_name` keyword argument with `id`",
        transformer=ReplaceKeyNameKwarg,
    ),
    Transformation(
        code="T007",
        description="Replace `key` method call with `key` attribute",
        transformer=ReplaceKeyCall,
    ),
    Transformation(
        code="T008",
        description="Replace `db.BlobProperty()` with `ndb.BlobProperty()`",
        transformer=ReplaceBlobProperty,
    ),
    Transformation(
        code="T009",
        description="Replace `db.BooleanProperty()` with `ndb.BooleanProperty()`",
        transformer=ReplaceBooleanProperty,
    ),
    Transformation(
        code="T010",
        description="Replace `db.ByteStringProperty()` with `ndb.BlobProperty(indexed=True)`",
        transformer=ReplaceByteStringProperty,
    ),
    Transformation(
        code="T011",
        description="Replace `db.CategoryProperty()` with `ndb.StringProperty()`",
        transformer=ReplaceCategoryProperty,
    ),
    Transformation(
        code="T012",
        description="Replace `db.DateProperty()` with `ndb.DateProperty()`",
        transformer=ReplaceDateProperty,
    ),
    Transformation(
        code="T013",
        description="Replace `db.DateTimeProperty()` with `ndb.DateTimeProperty()`",
        transformer=ReplaceDateTimeProperty,
    ),
    Transformation(
        code="T014",
        description="Replace `db.EmailProperty()` with `ndb.EmailProperty()`",
        transformer=ReplaceEmailProperty,
    ),
    Transformation(
        code="T015",
        description="Replace `db.FloatProperty()` with `ndb.FloatProperty()`",
        transformer=ReplaceFloatProperty,
    ),
    Transformation(
        code="T016",
        description="Replace `db.GeoPtProperty()` with `ndb.GeoPtProperty()`",
        transformer=ReplaceGeoPtProperty,
    ),
    Transformation(
        code="T017",
        description="Replace `db.IntegerProperty()` with `ndb.IntegerProperty()`",
        transformer=ReplaceIntegerProperty,
    ),
    Transformation(
        code="T018",
        description="Replace `db.LinkProperty()` with `ndb.StringProperty()`",
        transformer=ReplaceLinkProperty,
    ),
    Transformation(
        code="T019",
        description="Replace `db.ListProperty(bool)` with `ndb.BooleanProperty(repeated=True)`",
        transformer=ReplaceListPropertyBool,
    ),
    Transformation(
        code="T020",
        description="Replace `db.ListProperty(float)` with `ndb.FloatProperty(repeated=True)`",
        transformer=ReplaceListPropertyFloat,
    ),
    Transformation(
        code="T021",
        description="Replace `db.ListProperty(int)` with `ndb.IntegerProperty(repeated=True)`",
        transformer=ReplaceListPropertyInt,
    ),
    Transformation(
        code="T022",
        description="Replace `db.ListProperty(db.Key)` with `ndb.KeyProperty(repeated=True)`",
        transformer=ReplaceListPropertyDBKey,
    ),
    Transformation(
        code="T023",
        description="Replace `db.PhoneNumberProperty()` with `ndb.StringProperty()`",
        transformer=ReplacePhoneNumberProperty,
    ),
    Transformation(
        code="T024",
        description="Replace `db.PostalAddressProperty()` with `ndb.StringProperty()`",
        transformer=ReplacePostalAddressProperty,
    ),
    Transformation(
        code="T025",
        description="Replace `db.RatingProperty()` with `ndb.IntegerProperty()`",
        transformer=ReplaceRatingProperty,
    ),
    Transformation(
        code="T026",
        description=ReplaceReferenceProperty.__doc__,
        transformer=ReplaceReferenceProperty,
    ),
)
