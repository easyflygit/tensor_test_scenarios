from base.base_test import BaseTest
from time import sleep


class TestThirdScenario(BaseTest):
    """Класс для тестрирования третьего сценария"""
    def test_third_scenario(self):
        """Тестируем согласно первому тестовому заданию """
        self.sbis_index_page.open()
        self.sbis_index_page.scroll_to_footer()
        self.sbis_index_page.download_library_link_is_visible()
        self.sbis_index_page.click_download_library_link()
        self.sbis_download_report_page.plugin_tab_is_visible()
        self.sbis_download_report_page.click_plugin_tab()
        self.sbis_download_plugin_page.download_link_is_visible()
        self.sbis_download_plugin_page.click_download_link()
        self.sbis_download_plugin_page.check_plugin_downloaded()
        self.sbis_download_plugin_page.check_downloaded_file_size()

        sleep(2)