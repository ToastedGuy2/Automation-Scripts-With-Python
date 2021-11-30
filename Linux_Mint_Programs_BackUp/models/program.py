from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import StringField


class Program(Document):
    name = StringField(required=True, max_length=50)
    meta = {'allow_inheritance': True}
