from os import listdir, walk
from os.path import join, isdir, getmtime
from subprocess import run
from shutil import move
from typing import List
from .file_installer import FileInstaller
# TODO: Implement a raise Exception in constructor in case the filename is wrong


class TarXzInstaller(FileInstaller):
    def __init__(self, filename, appname) -> None:
        super().__init__(filename)
        self.appname = appname
        self.unzip_command = 'tar -xf'
        self.opt_directory = '/opt'
        self.desktop_shortcuts_directory = '/usr/share/applications'
        self.desktop_file_template = f"[Desktop Entry]\nType = Application\nName = {appname}\nIcon = PATH_TO_ICON\nExec = PATH_TO_APP"

    def unzip_file(self) -> str:
        run(f"{self.unzip_command} '{self.file_path}' -C {self.download_directory} --checkpoint=.100", shell=True, check=True)

    def get_subdirectories_from_downloads(self) -> List[str]:
        dir_tree = listdir(self.download_directory)
        return list(filter(lambda d: isdir(
            join(self.download_directory, d)),dir_tree ))

    def get_subdirectories_details_from_downloads(self) -> List[dict]:
        return list(map(lambda d: {'name': d, 'path': join(self.download_directory, d), 'modified_date': getmtime(join(self.download_directory, d))},self.get_subdirectories_from_downloads()))

    def get_extracted_file(self) -> str:
        sub_dirs = self.get_subdirectories_details_from_downloads()
        sub_dirs.sort(
            reverse=True, key=lambda d: d['modified_date'])
        return sub_dirs[0]

    def move_file_from_downloads_to_opt(self):
        extracted_file = self.get_extracted_file()
        source = join(self.download_directory, extracted_file['name'])
        run(f"sudo cp -r {source} {self.opt_directory} && rm -R {source}", shell=True, check=True)

    def find_icon_path(self):
        look_into = join(self.opt_directory, self.get_extracted_file()['name'])
        for root, dirs, files in walk(look_into):
            for file in files:
                if '128' in file and '.png' in file:
                    return join(root, file)

    def find_executable_path(self):
        look_into = join(self.opt_directory, self.get_extracted_file()['name'])
        for root, dirs, files in walk(look_into):
            for file in files:
                if '128' in file and '.png' in file:
                    return join(root, file)

    def create_desktop_shortcut(self):
        desktop_file_path_from_downloads = join(self.download_directory, self.appname + '.desktop')
        with open(desktop_file_path_from_downloads, 'w') as f:
            icon = self.find_icon_path()
            exec = self.find_executable_path()
            self.desktop_file_template = self.desktop_file_template.replace(
                'PATH_TO_ICON', icon)
            self.desktop_file_template = self.desktop_file_template.replace(
                'PATH_TO_APP', exec)
            f.write(self.desktop_file_template)
        run(f"mv {desktop_file_path_from_downloads} {self.desktop_shortcuts_directory}")

    def install(self):
        self.unzip_file()
        self.move_file_from_downloads_to_opt()
        self.create_desktop_shortcut()
