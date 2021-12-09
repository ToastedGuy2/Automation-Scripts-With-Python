from .extension import Extension
from .program import Program
from mongoengine.fields import EnumField, StringField


class WebScrap_Fetch_Link(Program):
    url = StringField(required=True)
    link_filter = StringField(required=True)
    ext = EnumField(Extension, default=Extension.DEB, required=True)
