import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

from db2ndb.transformers._builders import ReplaceListProperty, ReplaceProperty

__all__ = (
    "ReplaceBlobProperty",
    "ReplaceBooleanProperty",
    "ReplaceByteStringProperty",
    "ReplaceCategoryProperty",
    "ReplaceDateProperty",
    "ReplaceDateTimeProperty",
    "ReplaceEmailProperty",
    "ReplaceFloatProperty",
    "ReplaceGeoPtProperty",
    "ReplaceIntegerProperty",
    "ReplaceLinkProperty",
    "ReplaceListPropertyBool",
    "ReplaceListPropertyFloat",
    "ReplaceListPropertyInt",
    "ReplaceListPropertyDBKey",
    "ReplacePhoneNumberProperty",
    "ReplacePostalAddressProperty",
    "ReplaceRatingProperty",
    "ReplaceStringProperty",
    "RemoveMultilineKwarg",
    "ReplaceTextProperty",
    "ReplaceTimeProperty",
    "ReplaceUserProperty",
    "ReplaceBlobReferenceProperty",
)

ReplaceBlobProperty = ReplaceProperty("db.BlobProperty", "ndb.BlobProperty")
ReplaceBooleanProperty = ReplaceProperty("db.BooleanProperty", "ndb.BooleanProperty")
ReplaceCategoryProperty = ReplaceProperty("db.CategoryProperty", "ndb.StringProperty")
ReplaceDateProperty = ReplaceProperty("db.DateProperty", "ndb.DateProperty")
ReplaceDateTimeProperty = ReplaceProperty("db.DateTimeProperty", "ndb.DateTimeProperty")
ReplaceEmailProperty = ReplaceProperty("db.EmailProperty", "ndb.StringProperty")
ReplaceFloatProperty = ReplaceProperty("db.FloatProperty", "ndb.FloatProperty")
ReplaceGeoPtProperty = ReplaceProperty("db.GeoPtProperty", "ndb.GeoPtProperty")
ReplaceIntegerProperty = ReplaceProperty("db.IntegerProperty", "ndb.IntegerProperty")
ReplaceLinkProperty = ReplaceProperty("db.LinkProperty", "ndb.StringProperty")
ReplaceListPropertyBool = ReplaceListProperty("bool", "BooleanProperty")
ReplaceListPropertyFloat = ReplaceListProperty("float", "FloatProperty")
ReplaceListPropertyInt = ReplaceListProperty("int", "IntegerProperty")
ReplaceListPropertyDBKey = ReplaceListProperty("db.Key", "KeyProperty")
ReplacePhoneNumberProperty = ReplaceProperty(
    "db.PhoneNumberProperty", "ndb.StringProperty"
)
ReplacePostalAddressProperty = ReplaceProperty(
    "db.PostalAddressProperty", "ndb.StringProperty"
)
ReplaceRatingProperty = ReplaceProperty("db.RatingProperty", "ndb.IntegerProperty")
ReplaceStringProperty = ReplaceProperty("db.StringProperty", "ndb.StringProperty")
ReplaceTextProperty = ReplaceProperty("db.TextProperty", "ndb.TextProperty")
ReplaceTimeProperty = ReplaceProperty("db.TimeProperty", "ndb.TimeProperty")
ReplaceUserProperty = ReplaceProperty("db.UserProperty", "ndb.UserProperty")
ReplaceBlobReferenceProperty = ReplaceProperty(
    "blobstore.BlobReferenceProperty", "ndb.BlobKeyProperty"
)


class ReplaceByteStringProperty(ContextAwareTransformer):
    @m.leave(
        m.Call(
            func=m.Attribute(
                value=m.Name(value="db"), attr=m.Name(value="ByteStringProperty")
            )
        )
    )
    def _transform(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        return updated_node.with_changes(
            func=cst.Attribute(
                value=cst.Name(value="ndb"),
                attr=cst.Name(value="BlobProperty"),
            ),
            args=[
                *updated_node.args,
                cst.Arg(
                    value=cst.Name(value="True"),
                    keyword=cst.Name(value="indexed"),
                    equal=cst.AssignEqual(
                        whitespace_after=cst.SimpleWhitespace(value=""),
                        whitespace_before=cst.SimpleWhitespace(value=""),
                    ),
                ),
            ],
        )


class RemoveMultilineKwarg(ContextAwareTransformer):
    @m.leave(m.Arg(keyword=m.Name(value="multiline")))
    def _transform(
        self, original_node: cst.Arg, updated_node: cst.Arg
    ) -> cst.RemovalSentinel:
        return cst.RemoveFromParent()
