from dataclasses import dataclass

from db2ndb.transformers import (
    RemoveMultilineKwarg,
    ReplaceBlobProperty,
    ReplaceBlobReferenceProperty,
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
    ReplaceSelfReferenceProperty,
    ReplaceStringProperty,
    ReplaceTextProperty,
    ReplaceTimeProperty,
    ReplaceUserProperty,
)
from db2ndb.typing import TransformerType

__all__ = ("TRANSFORMATIONS",)


@dataclass
class Transformation:
    code: str
    transformer: TransformerType


TRANSFORMATIONS = (
    Transformation(
        code="T001",
        transformer=ReplaceDBModelBase,
    ),
    Transformation(
        code="T002",
        transformer=ReplaceKindDef,
    ),
    Transformation(
        code="T003",
        transformer=ReplaceKindCall,
    ),
    Transformation(
        code="T004",
        transformer=ReplacePropertiesCall,
    ),
    Transformation(
        code="T005",
        transformer=ReplaceDynamicPropertiesCall,
    ),
    Transformation(
        code="T006",
        transformer=ReplaceKeyNameKwarg,
    ),
    Transformation(
        code="T007",
        transformer=ReplaceKeyCall,
    ),
    Transformation(
        code="T008",
        transformer=ReplaceBlobProperty,
    ),
    Transformation(
        code="T009",
        transformer=ReplaceBooleanProperty,
    ),
    Transformation(
        code="T010",
        transformer=ReplaceByteStringProperty,
    ),
    Transformation(
        code="T011",
        transformer=ReplaceCategoryProperty,
    ),
    Transformation(
        code="T012",
        transformer=ReplaceDateProperty,
    ),
    Transformation(
        code="T013",
        transformer=ReplaceDateTimeProperty,
    ),
    Transformation(
        code="T014",
        transformer=ReplaceEmailProperty,
    ),
    Transformation(
        code="T015",
        transformer=ReplaceFloatProperty,
    ),
    Transformation(
        code="T016",
        transformer=ReplaceGeoPtProperty,
    ),
    Transformation(
        code="T017",
        transformer=ReplaceIntegerProperty,
    ),
    Transformation(
        code="T018",
        transformer=ReplaceLinkProperty,
    ),
    Transformation(
        code="T019",
        transformer=ReplaceListPropertyBool,
    ),
    Transformation(
        code="T020",
        transformer=ReplaceListPropertyFloat,
    ),
    Transformation(
        code="T021",
        transformer=ReplaceListPropertyInt,
    ),
    Transformation(
        code="T022",
        transformer=ReplaceListPropertyDBKey,
    ),
    Transformation(
        code="T023",
        transformer=ReplacePhoneNumberProperty,
    ),
    Transformation(
        code="T024",
        transformer=ReplacePostalAddressProperty,
    ),
    Transformation(
        code="T025",
        transformer=ReplaceRatingProperty,
    ),
    Transformation(
        code="T026",
        transformer=ReplaceReferenceProperty,
    ),
    Transformation(
        code="T027",
        transformer=ReplaceSelfReferenceProperty,
    ),
    Transformation(
        code="T028",
        transformer=ReplaceStringProperty,
    ),
    Transformation(
        code="T029",
        transformer=RemoveMultilineKwarg,
    ),
    # Transformation(
    #     code="T030",
    #     transformer=ReplaceStringListProperty,
    # ),
    Transformation(
        code="T031",
        transformer=ReplaceTextProperty,
    ),
    Transformation(
        code="T032",
        transformer=ReplaceTimeProperty,
    ),
    Transformation(
        code="T033",
        transformer=ReplaceUserProperty,
    ),
    Transformation(
        code="T034",
        transformer=ReplaceBlobReferenceProperty,
    ),
)
