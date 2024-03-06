import os
from time import sleep

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class SbisDownloadReportPage(BasePage):
    """Класс для страницы 'https://sbis.ru/download?tab=report&innerTab=report25'"""
    PAGE_URL = Links.SBIS_DOWNLOAD_REPORT_PAGE

    PLUGIN_TAB_HIDDEN = ("xpath", '(//div[@class="controls-TabButton__inner"])[2]')
    PLUGIN_TAB = ("xpath", '//div[@data-id="plugin"]')

    def plugin_tab_is_visible(self):
        self.wait.until(EC.presence_of_element_located(self.PLUGIN_TAB))

    def click_plugin_tab(self):
        plugin_tab = self.wait.until(EC.element_to_be_clickable(self.PLUGIN_TAB))
        hidden_submenu = self.wait.until(EC.visibility_of_element_located(self.PLUGIN_TAB_HIDDEN))
        ActionChains(self.driver).move_to_element(plugin_tab).click(hidden_submenu).perform()


class SbisDownloadPluginPage(BasePage):
    """Класс для страницы 'https://sbis.ru/download?tab=plugin&innerTab=default'"""
    PAGE_URL = Links.SBIS_DOWNLOAD_PLUGIN_PAGE

    DOWNLOAD_LINK = ("xpath", '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

    def download_link_is_visible(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_LINK))

    def click_download_link(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_LINK)).click()

    def check_plugin_downloaded(self):
        while not os.path.isfile('downloads/sbisplugin-setup-web.exe'):
            sleep(2)
        if os.path.isfile('downloads/sbisplugin-setup-web.exe'):
            sleep(2)
            print("File download is completed")
        else:
            print("File download is not completed")

    def check_downloaded_file_size(self):
        file_stats = os.stat("downloads/sbisplugin-setup-web.exe")
        print(f'File Size in Bytes is {file_stats.st_size}')
        print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
        rounded_file_size = round(float(f"{file_stats.st_size}") / (1024 * 1024), 2)
        print(f'File Size in MegaBytes(rounded) is {rounded_file_size}')
        assert rounded_file_size == 8.17, "File size isn't equal to original file"





