from subprocess import run
from typing import List


class TerminalInstaller():
    def __init__(self) -> None:
        self.root_password = 'peel-shift-auto'
        self.authentication = f'echo {self.root_password} | sudo -S'
        self.update_command = 'sudo apt-get update'
        self.upgrade_command = 'sudo apt upgrade -y'
        self.full_command = f'{self.authentication} {self.update_command} && {self.upgrade_command}'

    def concatenate_commands(self, commands: List[str]) -> str:
        return ' && '.join(commands)

    def get_final_command(self, commands: List[str]) -> str:
        return f'{self.full_command} && {self.concatenate_commands(commands)}'

    def install_program(self, commands: List[str]) -> None:
        run(self.get_final_command(commands))
