from unittest import TestCase
from unittest.mock import MagicMock, patch, mock_open
from requests import get
from requests.models import Response
from tempfile import TemporaryFile, mkstemp
from platform import system
from helpers.file_helper import get_file_path
import logic


class TestDownloader(TestCase):
    def test_download_directory_using_temporary_files_directory(self):
        # hello_world
        r = Response()
        r._content = bytes('hello_world', 'utf-8')
        # r.content = bytes('hello_world', 'utf-8')
        get = MagicMock(return_value=r)
        r = get('https://duckduckgo.com/')
        filepath = get_file_path("I'm a txt file.txt")
        tp = TemporaryFile()
        tp.write(r.content)
        tp.seek(0)
        content = tp.read().decode("utf-8")
        self.assertEqual(content, 'hello_world')
        get.assert_called_once_with('https://duckduckgo.com/')
        tp.close()

    def test_download_directory_using_patch(self):
        r = Response()
        r._content = bytes('hello_world', 'utf-8')
        get_mock = MagicMock(return_value=r)
        # get = get_mock
        # patch('logic.downloader.get', get_mock, create=True)
        with patch('requests.get', get_mock, create=True):
            open_mock = mock_open()
            with patch("logic.downloader.open", open_mock, create=True):
                filename = 'hello_world.txt'
                filepath = get_file_path(filename)
                logic.downloader.download_file(
                    "https://duckduckgo.com/", filename)
                open_mock.assert_called_with(filepath, "wb")
                get_mock.assert_called_with("https://duckduckgo.com/")
                open_mock.return_value.write.assert_called_once_with(
                    b'hello_world')
