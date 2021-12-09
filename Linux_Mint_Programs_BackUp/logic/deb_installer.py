from .file_installer import FileInstaller
from subprocess import run


class DebInstaller(FileInstaller):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.deb_install_command = 'sudo dpkg -i'
        self.install_command = f'{self.deb_install_command} {self.file_path}'

    def install(self):
        run(self.install_command)
