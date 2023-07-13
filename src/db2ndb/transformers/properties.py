import libcst as cst
import libcst.matchers as m
from libcst.codemod import ContextAwareTransformer

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
    "ReplacePhoneNumberProperty",
    "ReplacePostalAddressProperty",
    "ReplaceRatingProperty",
    "ReplaceStringProperty",
    "ReplaceTextProperty",
    "ReplaceTimeProperty",
    "ReplaceUserProperty",
    "ReplaceBlobReferenceProperty",
)


def ReplaceProperty(before: str, after: str) -> ContextAwareTransformer:
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

    return _ReplaceProperty


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
