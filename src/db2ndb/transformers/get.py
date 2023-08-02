import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

__all__ = ("ReplaceGetByKeyNameCall", "ReplaceDBGetCall")


class ReplaceGetByKeyNameCall(ContextAwareTransformer):
    """Replace `MyModel.get_by_key_name('my_key')` with `MyModel.get_by_id('my_key')`"""

    @m.call_if_inside(m.Call(func=m.Attribute(attr=m.Name(value="get_by_key_name"))))
    @m.leave(m.Attribute(attr=m.Name(value="get_by_key_name")))
    def _transform(
        self, original_node: cst.Attribute, updated_node: cst.Attribute
    ) -> cst.Attribute:
        return updated_node.with_changes(attr=cst.Name(value="get_by_id"))


class ReplaceDBGetCall(ContextAwareTransformer):
    """Replace `db.get(key)` call with `key.get()`"""

    @m.leave(
        m.Call(func=m.Attribute(value=m.Name(value="db"), attr=m.Name(value="get")))
    )
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        key_arg = None
        other_args = []

        for i, arg in enumerate(updated_node.args):
            print(arg)
            if key_arg is None:
                if (i == 0 and arg.keyword is None) or arg.keyword.value == "keys":
                    key_arg = arg
                    continue

            other_args.append(arg)

        assert key_arg is not None, "Key not found"

        return cst.Call(
            func=cst.Attribute(
                value=key_arg.value,
                attr=cst.Name(
                    value="get",
                ),
            ),
        )
