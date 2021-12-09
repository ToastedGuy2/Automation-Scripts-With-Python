from subprocess import run
from typing import List
from .installer import Installer


class TerminalInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()

    def install(self, commands: List[str]):
        self.run_default_commands()
        for command in commands:
            run(command)
