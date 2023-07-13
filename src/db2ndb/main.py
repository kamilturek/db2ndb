from typing import Optional, Sequence

import libcst as cst
from libcst.codemod import CodemodContext
from libcst.codemod.visitors import AddImportsVisitor, RemoveImportsVisitor

from db2ndb.transformations import TRANSFORMATIONS
from db2ndb.typing import TransformerType


def transform(source: str, transformer_types: Sequence[TransformerType]) -> str:
    tree = cst.parse_module(source)

    transformer_types = [
        *transformer_types,
        AddImportsVisitor,
        RemoveImportsVisitor,
    ]

    context = CodemodContext()
    for transformer_type in transformer_types:
        transformer = transformer_type(context)
        tree = transformer.transform_module(tree)

    return tree.code


def gather_transformers(disabled: Optional[Sequence[str]] = None):
    if disabled is None:
        disabled = []

    return [
        transformation.transformer
        for transformation in TRANSFORMATIONS
        if transformation.code not in disabled
    ] + [
        AddImportsVisitor,
        RemoveImportsVisitor,
    ]
