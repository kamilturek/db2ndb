import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

__all__ = ("ReplaceBlobProperty",)


class ReplaceBlobProperty(ContextAwareTransformer):
    @m.leave(m.Attribute(value=m.Name(value="db"), attr=m.Name(value="BlobProperty")))
    def _transform(
        self, original_node: cst.Attribute, updated_node: cst.Attribute
    ) -> cst.Attribute:
        return updated_node.with_changes(
            value=cst.Name(value="ndb"), attr=cst.Name(value="BlobProperty")
        )
