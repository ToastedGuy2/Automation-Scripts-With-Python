from unittest import TestCase
from models.extension import Extension
from helpers.file_helper import get_filename


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
