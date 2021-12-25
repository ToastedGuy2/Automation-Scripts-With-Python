from models.extension import Extension
from os.path import expanduser, join


def get_filename(name: str, ext: Extension) -> str:
    return name + ext


def get_file_path(filename: str) -> str:
    return join(expanduser('~'), 'Downloads', filename)
