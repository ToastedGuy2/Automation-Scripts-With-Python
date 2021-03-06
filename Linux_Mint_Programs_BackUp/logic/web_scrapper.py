from typing import List
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class WebScrapper():
    def __init__(self) -> None:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def get_download_link(self, url: str, a_tag_filter: str) -> str:
        self.driver.get(url)
        links = self.driver.find_elements(by=By.TAG_NAME, value='a')
        download_links = list(
            filter(lambda l: a_tag_filter in l.get_attribute('href'), links))
        download_link = download_links[0].get_attribute('href') if len(
            download_links) > 0 else None
        self.driver.quit()
        return download_link

    def get_terminal_commands(self, docs_url: str, css_selector: str, start: int = 0, end: int = 0) -> List[str]:
        self.driver.get(docs_url)
        commands_list = self.driver.find_elements(
            by=By.CSS_SELECTOR, value=css_selector)
        installation_commands = commands_list[start: end+1]
        return self.clean_commands(installation_commands)

    def clean_commands(self, commands: List[str]) -> str:
        final_commands = []
        for c in commands:
            sub_commands = c.text.split('\n')
            filtered_subcommands = filter(
                lambda s: '#' not in s and s.strip() != '', sub_commands)
            for fil in filtered_subcommands:
                final_commands.append(fil)
        self.driver.quit()
        return final_commands
