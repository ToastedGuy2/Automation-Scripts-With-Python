from os.path import join
from unittest import TestCase
from unittest.mock import patch, MagicMock
from logic.file_installer import FileInstaller


class TestFileInstaller(TestCase):
    def setUp(self) -> None:
        self.home_directory = '/home/me'
        self.downlads_directory = join(self.home_directory, 'Downloads',)
        self.filename = 'google_chrome.deb'
        self.file_path = join(self.downlads_directory, self.filename)

    def test_constructor_initialized_as_expected(self):
        with patch('logic.file_installer.expanduser', MagicMock(return_value=self.home_directory)) as mock_expanduser, patch('logic.file_installer.FileInstaller.run_default_commands', MagicMock(return_value=0)) as mock_run_default_commands, patch('logic.file_installer.exists', MagicMock(return_value=True)) as mock_exists:
            f = FileInstaller(self.filename)
            mock_expanduser.assert_called_once_with('~')
            self.assertEqual(f.download_directory,
                             self.downlads_directory)
            self.assertEqual(
                f.file_path, self.file_path)
            mock_run_default_commands.assert_called_once()
            mock_exists.assert_called_once_with(
                self.file_path)

    def test_constructor_throws_an_exception(self):
        with patch('logic.file_installer.expanduser', MagicMock(return_value=self.home_directory)) as mock_expanduser, patch('logic.file_installer.FileInstaller.run_default_commands', MagicMock(return_value=0)) as mock_run_default_commands, patch('logic.file_installer.exists', MagicMock(return_value=False)) as mock_exists:
            self.assertRaises(ValueError, FileInstaller, self.filename)
            mock_expanduser.assert_called_once_with('~')
            mock_exists.assert_called_once_with(
                self.file_path)
            mock_run_default_commands.assert_not_called()
