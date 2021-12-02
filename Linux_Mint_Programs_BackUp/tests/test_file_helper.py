from unittest import TestCase
from platform import system
from getpass import getuser
from models.extension import Extension
from helpers.file_helper import get_filename, get_file_path, get_download_directory


class TestFileHelper(TestCase):
    def test_get_file_name(self):
        actual = get_filename('hello_world', Extension.DEB)
        expected = 'hello_world.deb'
        self.assertEqual(expected, actual)
        actual = get_filename("i'm a file", Extension.APPIMAGE)
        expected = "i'm a file.AppImage"
        self.assertEqual(expected, actual)
        actual = get_filename("filename", Extension.TAR_XZ)
        expected = "filename.tar.xz"
        self.assertEqual(expected, actual)

    def test_get_download_directory_for_linux_distributions(self):
        if(system() == 'Linux'):
            expected = f'/home/{getuser()}/Downloads'
            actual = get_download_directory()
            self.assertEqual(expected, actual)

    def test_get_file_path(self):
        if(system() == 'Linux'):
            filename = get_filename('demo', Extension.DEB)
            actual = get_file_path(filename)
            expected = f'/home/{getuser()}/Downloads/demo.deb'
            self.assertEqual(expected, actual)
