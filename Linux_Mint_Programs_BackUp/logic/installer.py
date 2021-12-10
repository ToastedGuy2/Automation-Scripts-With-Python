from subprocess import run


class Installer():
    def __init__(self) -> None:
        self.root_password = 'peel-shift-auto'
        self.authentication_command = f'echo {self.root_password} | sudo -S'
        self.update_command = 'sudo apt-get update'
        self.upgrade_command = 'sudo apt upgrade -y'
        self.default_command = f'{self.authentication_command} {self.update_command} && {self.upgrade_command}'

    def run_default_commands(self) -> int:
        return run(self.default_command, shell=True, check=True)
