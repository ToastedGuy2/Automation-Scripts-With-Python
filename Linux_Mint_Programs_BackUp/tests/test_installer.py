from unittest import TestCase
from unittest.mock import MagicMock, patch
from logic.installer import Installer


class TestInstaller(TestCase):
    def test_run_default_commands_correctly(self):
        i = Installer()
        with patch('logic.installer.run', return_value=0) as mock_run:
            i.run_default_commands()
            mock_run.assert_called_once_with(
                'echo peel-shift-auto | sudo -S sudo apt-get update && sudo apt upgrade -y', check=True)
