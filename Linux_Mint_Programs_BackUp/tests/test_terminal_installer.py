from subprocess import call
from unittest import TestCase
from unittest.mock import MagicMock, patch, call
from logic.terminal_installer import TerminalInstaller


class TestTerminalInstaller(TestCase):
    def test_install(self):
        with patch('logic.terminal_installer.Installer.run_default_commands') as mock_run_default_commands, patch('logic.terminal_installer.run', MagicMock(return_value=0)) as mock_run:
            t = TerminalInstaller()
            command_1 = 'wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb'
            command_2 = 'sudo dpkg -i packages-microsoft-prod.deb'
            command_3 = 'rm packages-microsoft-prod.deb', 'sudo apt-get update; \
                                                            sudo apt-get install -y apt-transport-https && \
                                                            sudo apt-get update && \
                                                            sudo apt-get install -y dotnet-sdk-6.0'
            commands = [command_1, command_2, command_3]
            t.install(commands)
            mock_run_default_commands.assert_called_once()
            mock_run.assert_has_calls(
                [call(command_1), call(command_2), call(command_3)])
