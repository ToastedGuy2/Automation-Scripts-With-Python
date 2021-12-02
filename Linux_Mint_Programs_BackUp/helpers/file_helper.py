from models.extension import Extension
from os.path import expanduser, join


def get_filename(name: str, ext: Extension) -> str:
    return name + ext.value


def get_download_directory() -> str:
    home_directory = expanduser('~')
    return join(home_directory, 'Downloads')


def get_file_path(filename: str) -> str:
    return join(get_download_directory(), filename)
