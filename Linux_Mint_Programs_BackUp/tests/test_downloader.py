from unittest import TestCase
from unittest.mock import MagicMock, patch, mock_open
from requests import get
from requests.models import Response
from tempfile import TemporaryFile, mkstemp
from platform import system
from helpers.file_helper import get_file_path
import logic


class TestDownloader(TestCase):
    def setUp(self) -> None:
        self.r = Response()
        self.r._content = bytes('hello_world', 'utf-8')
        self.get_mock = MagicMock(return_value=self.r)
        self.tp = TemporaryFile()

    def tearDown(self) -> None:
        self.tp.close()

    def test_download_directory_using_temporary_files_directory(self):
        # with patch(target='requests.get', new=self.get_mock, create=True):
        r = self.get_mock('https://duckduckgo.com/')
        self.tp.write(r.content)
        self.tp.seek(0)
        content = self.tp.read().decode("utf-8")
        self.assertEqual(content, 'hello_world')
        self.get_mock.assert_called_once_with('https://duckduckgo.com/')

    def test_download_directory_using_patch(self):
        with patch('logic.downloader.get', return_value=self.r, create=True) as g:
            open_mock = mock_open()
            with patch("logic.downloader.open", open_mock, create=True):
                filename = 'hello_world.txt'
                filepath = get_file_path(filename)
                logic.downloader.download_file(
                    "https://duckduckgo.com/", filename)
                open_mock.assert_called_with(filepath, "wb")
                g.assert_called_with("https://duckduckgo.com/")
                open_mock.return_value.write.assert_called_once_with(
                    b'hello_world')
