from typing import Callable, Type, Union

from libcst.codemod import CodemodContext, ContextAwareTransformer

TransformerType = Union[
    Type[ContextAwareTransformer],
    Callable[[CodemodContext], ContextAwareTransformer],
]
