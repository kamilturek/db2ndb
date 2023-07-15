import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer


def ReplaceProperty(
    before: str, after: str, docstring: str = ""
) -> ContextAwareTransformer:
    before_value, before_attr = before.split(".")
    after_value, after_attr = after.split(".")

    class _ReplaceProperty(ContextAwareTransformer):
        @m.leave(
            m.Attribute(
                value=m.Name(value=before_value), attr=m.Name(value=before_attr)
            )
        )
        def _transform(
            self, original_node: cst.Attribute, updated_node: cst.Attribute
        ) -> cst.Attribute:
            return updated_node.with_changes(
                value=cst.Name(value=after_value), attr=cst.Name(value=after_attr)
            )

    if docstring:
        ReplaceProperty.__doc__ = docstring

    return _ReplaceProperty


def ReplaceListProperty(arg: str, prop: str) -> ContextAwareTransformer:
    if "." in arg:
        value, attr = arg.split(".")
        matcher = m.Attribute(value=m.Name(value=value), attr=m.Name(value=attr))
    else:
        matcher = m.Name(value=arg)

    class _ReplaceListProperty(ContextAwareTransformer):
        @m.leave(
            m.Call(
                func=m.Attribute(
                    value=m.Name(value="db"),
                    attr=m.Name(value="ListProperty"),
                ),
                args=(m.Arg(value=matcher),),
            )
        )
        def _transform(
            self, original_node: cst.Call, updated_node: cst.Call
        ) -> cst.Call:
            return updated_node.with_changes(
                func=cst.Attribute(
                    value=cst.Name(value="ndb"), attr=cst.Name(value=prop)
                ),
                args=(
                    cst.Arg(
                        value=cst.Name(value="True"),
                        keyword=cst.Name(value="repeated"),
                        equal=cst.AssignEqual(
                            whitespace_after=cst.SimpleWhitespace(value=""),
                            whitespace_before=cst.SimpleWhitespace(value=""),
                        ),
                    ),
                ),
            )

    return _ReplaceListProperty
