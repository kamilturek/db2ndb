from dataclasses import dataclass

from db2ndb.transformers import (
    ReplaceBlobProperty,
    ReplaceDBModelBase,
    ReplaceDynamicPropertiesCall,
    ReplaceKeyCall,
    ReplaceKeyNameKwarg,
    ReplaceKindCall,
    ReplaceKindDef,
    ReplacePropertiesCall,
)
from db2ndb.typing import TransformerType

__all__ = ("TRANSFORMATIONS",)


@dataclass
class Transformation:
    code: str
    description: str
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
        description="Replace `dynamic_properties` method call with `_properties` attribute",
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
    )
)
