from requests import get
from ..helpers.file_helper import get_file_path


def download_file(url: str, filename: str):
    r = get(url)
    filepath = get_file_path(filename)
    with open(filepath, 'wb') as f:
        f.write(r.content)
