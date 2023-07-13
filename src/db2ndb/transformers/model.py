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
    @m.leave(m.FunctionDef(name=m.Name(value="kind")))
    def _transform(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        return updated_node.with_changes(name=cst.Name(value="_get_kind"))


class ReplaceKindCall(ContextAwareTransformer):
    @m.call_if_inside(m.Call(func=m.Attribute(attr=m.Name(value="kind"))))
    @m.leave(m.Attribute(attr=m.Name(value="kind")))
    def _transform(
        self, original_node: cst.Attribute, updated_node: cst.Attribute
    ) -> cst.Attribute:
        return updated_node.with_changes(attr=cst.Name(value="_get_kind"))


class ReplacePropertiesCall(ContextAwareTransformer):
    @m.leave(m.Call(func=m.Attribute(attr=m.Name(value="properties"))))
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        return cst.Attribute(
            value=updated_node.func.value, attr=cst.Name(value="_properties")
        )


class ReplaceDynamicPropertiesCall(ContextAwareTransformer):
    @m.leave(m.Call(func=m.Attribute(attr=m.Name(value="dynamic_properties"))))
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        return cst.Attribute(
            value=updated_node.func.value, attr=cst.Name(value="_properties")
        )
