import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

__all__ = ("ReplaceDBPutCall",)


class ReplaceDBPutCall(ContextAwareTransformer):
    """Replace `db.put(model_instance)` with `model_instance.put()`"""

    @m.leave(
        m.Call(func=m.Attribute(value=m.Name(value="db"), attr=m.Name(value="put")))
    )
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        model_arg = None
        other_args = []

        for i, arg in enumerate(updated_node.args):
            if model_arg is None:
                if (i == 0 and arg.keyword is None) or arg.keyword.value == "models":
                    model_arg = arg
                    continue

            other_args.append(arg)

        assert model_arg is not None, "Model not found"

        return cst.Call(
            func=cst.Attribute(
                value=model_arg.value,
                attr=cst.Name(
                    value="put",
                ),
            ),
        )
