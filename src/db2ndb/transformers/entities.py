import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

__all__ = ("ReplaceKeyNameKwarg", "ReplaceKeyCall")


class ReplaceKeyNameKwarg(ContextAwareTransformer):
    """Replace `key_name` keyword argument with `id`"""

    @m.leave(m.Arg(keyword=m.Name(value="key_name")))
    def _transform(self, original_node: cst.Arg, updated_node: cst.Arg) -> cst.Arg:
        return updated_node.with_changes(keyword=cst.Name(value="id"))


class ReplaceKeyCall(ContextAwareTransformer):
    """Replace `key` method call with `key` attribute"""

    @m.leave(m.Call(func=m.Attribute(attr=m.Name(value="key"))))
    def _transform(
        self, original_node: cst.Call, updated_node: cst.Call
    ) -> cst.Attribute:
        return cst.Attribute(value=updated_node.func.value, attr=cst.Name(value="key"))
