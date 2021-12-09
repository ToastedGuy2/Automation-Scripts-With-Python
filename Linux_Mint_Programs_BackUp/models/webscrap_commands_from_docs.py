from .program import Program
from mongoengine.fields import IntField, StringField


class WebScrap_Fetch_Commands(Program):
    docs_url = StringField(required=True)
    css_selector = StringField(required=True)
    start_extraction_on_command = IntField(min_value=0, default=0)
    end_extraction_on_command = IntField(required=True, min_value=0, default=0)
