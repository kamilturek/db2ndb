import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

__all__ = (
    "ReplaceDBModelBase",
    "ReplaceKindDef",
    "ReplaceKindCall",
    "ReplacePropertiesCall",
    "ReplaceDynamicPropertiesCall",
)


class ReplaceDBModelBase(ContextAwareTransformer):
    """Replace `class MyModel(db.Model)` with `class MyModel(ndb.Model)`"""

    @m.call_if_inside(
        m.ClassDef(
            bases=[
                m.AtLeastN(
                    n=1,
                    matcher=m.Arg(
                        value=m.Attribute(
                            value=m.Name(value="db"), attr=m.Name(value="Model")
                        )
                    ),
                )
            ]
        )
    )
    @m.leave(m.Attribute(value=m.Name(value="db"), attr=m.Name(value="Model")))
    def _transform(
        self, original_node: cst.Attribute, updated_node: cst.Attribute
    ) -> cst.Attribute:
        return updated_node.with_changes(value=cst.Name(value="ndb"))


class ReplaceKindDef(ContextAwareTransformer):
    """Replace `def kind(cls):` with `def _get_kind(cls):`"""

    @m.leave(m.FunctionDef(name=m.Name(value="kind")))
    def _transform(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        return updated_node.with_changes(name=cst.Name(value="_get_kind"))


class ReplaceKindCall(ContextAwareTransformer):
    """Replace `MyModel.kind()` with `MyModel._get_kind()`"""

    @m.call_if_inside(m.Call(func=m.Attribute(attr=m.Name(value="kind"))))
    @m.leave(m.Attribute(attr=m.Name(value="kind")))
    def _transform(
        self, original_node: cst.Attribute, updated_node: cst.Attribute
    ) -> cst.Attribute:
        return updated_node.with_changes(attr=cst.Name(value="_get_kind"))


class ReplacePropertiesCall(ContextAwareTransformer):
    """Replace `MyModel.properties()` with `MyModel._properties`"""

    @m.leave(m.Call(func=m.Attribute(attr=m.Name(value="properties"))))
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        return cst.Attribute(
            value=updated_node.func.value, attr=cst.Name(value="_properties")
        )


class ReplaceDynamicPropertiesCall(ContextAwareTransformer):
    """Replace `MyExpando.dynamic_properties()` with `MyExpando._properties`"""

    @m.leave(m.Call(func=m.Attribute(attr=m.Name(value="dynamic_properties"))))
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        return cst.Attribute(
            value=updated_node.func.value, attr=cst.Name(value="_properties")
        )
