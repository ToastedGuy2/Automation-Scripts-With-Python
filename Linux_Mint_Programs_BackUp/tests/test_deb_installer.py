from unittest import TestCase
from unittest.mock import MagicMock, patch
from logic.deb_installer import DebInstaller


class TestDebInstaller(TestCase):
    def test_install(self):
        with patch('logic.file_installer.exists', MagicMock(return_value=True)) as mock_exists, patch('logic.installer.Installer.run_default_commands', MagicMock(return_value=0)) as mock_run_default_commands,  patch('logic.deb_installer.run', MagicMock(return_value=0)) as mock_run:
            deb = DebInstaller('vscode.deb')
            deb.install()
            mock_exists.assert_called_once()
            mock_run_default_commands.assert_called_once()
            mock_run.assert_called_once()
