from unittest import TestCase
from unittest.mock import MagicMock, patch
from logic.app_image_installer import AppImageInstaller


class TestAppImageInstaller(TestCase):
    @patch('logic.app_image_installer.run')
    @patch('logic.app_image_installer.move')
    @patch('logic.app_image_installer.super')
    def test_install(self,  mock_super: MagicMock, mock_move: MagicMock, mock_run: MagicMock):
        a = AppImageInstaller('hello_world.txt')
        a.install()
        mock_super.assert_called_once()
        mock_move.assert_called_once()
        mock_run.assert_called_once()
