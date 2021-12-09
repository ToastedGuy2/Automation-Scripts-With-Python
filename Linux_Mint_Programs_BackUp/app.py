from platform import system
from queue import Queue
from models.terminal import Terminal
from models.webscrap_download_link import WebScrap_Fetch_Link
from models.webscrap_commands_from_docs import WebScrap_Fetch_Commands
from logic.terminal_installer import TerminalInstaller
from models.extension import Extension
from logic.web_scrapper import WebScrapper
from logic.deb_installer import DebInstaller
from logic.app_image_installer import AppImageInstaller
from logic.tar_xz_installer import TarXzInstaller
from logic.program_repository import ProgramRepository
from logic.downloader import download_file
from helpers.file_helper import get_filename
os = system()
if os == 'Linux':
    programs_queue = Queue()
    pr = ProgramRepository()
    for program in pr.get_all():
        programs_queue.put(program)
    while(programs_queue.qsize() > 0):
        program = programs_queue.get()
        if isinstance(program, Terminal):
            t = TerminalInstaller()
            t.install(program.commands)
        elif isinstance(program, WebScrap_Fetch_Link):
            ext = program.ext.value
            filename = get_filename(program.name, ext)
            w = WebScrapper()
            url = w.get_download_link(program.url, program.link_filter)
            download_file(url, filename)
            if ext == Extension.DEB.value:
                deb = DebInstaller(filename)
                deb.install()
            elif ext == Extension.APPIMAGE:
                a = AppImageInstaller(filename)
                a.install()
            elif ext == Extension.TAR_XZ:
                tar_xz = TarXzInstaller(filename, program.name)
                tar_xz.install()
        elif isinstance(program, WebScrap_Fetch_Commands):
            w = WebScrapper()
            commands = w.get_terminal_commands(
                program.docs_url, program.css_selector, program.start_extraction_on_command, program.end_extraction_on_command)
            t = TerminalInstaller()
            t.install(commands)
    print(f'{program.name} installed successfully')
