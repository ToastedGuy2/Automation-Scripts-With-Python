from .program import Program
from mongoengine.fields import ListField, StringField


class Terminal(Program):
    commands = ListField(StringField(max_length=200))
