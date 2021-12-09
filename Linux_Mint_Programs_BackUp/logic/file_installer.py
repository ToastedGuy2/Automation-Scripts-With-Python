from .installer import Installer
from os.path import expanduser, join, exists
from varname import nameof


class FileInstaller(Installer):
    def __init__(self, filename) -> None:
        super().__init__()
        self.home_directory = expanduser('~')
        self.download_directory = join(self.home_directory, 'Downloads')
        self.file_path = join(self.download_directory, filename)
        if not exists(self.file_path):
            raise ValueError(
                f"{nameof(filename)} provided doesn't exist within the Download Directory")
        self.run_default_commands()
