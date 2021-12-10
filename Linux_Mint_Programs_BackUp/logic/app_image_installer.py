from os.path import join
from shutil import move
from subprocess import run
from .file_installer import FileInstaller


class AppImageInstaller(FileInstaller):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.desktop_directory = join(self.home_directory, 'Desktop')
        self.file_desktop_path = join(self.desktop_directory, filename)
        self.grant_executable_rights_command = 'chmod u+x'

    def install(self) -> None:
        # Move file from downloads to desktop
        move(self.file_path, self.desktop_directory)
        # Grant file executable permissions
        run(f'{self.grant_executable_rights_command} {self.file_desktop_path}',
            shell=True, check=True)
