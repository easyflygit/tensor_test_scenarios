from base.base_test import BaseTest


class TestThirdScenario(BaseTest):
    """Класс для тестрирования третьего сценария"""
    def test_third_scenario(self):
        """Тестируем согласно первому тестовому заданию """
        # Открываем 'https://sbis.ru'
        self.sbis_index_page.open()
        # Прокручиваем страницу до блока Footer
        self.sbis_index_page.scroll_to_footer()
        # Находим кнопку "Скачать локальные версии"
        self.sbis_index_page.download_library_link_is_visible()
        # Кликаем на кнопку "Скачать локальные версии"
        self.sbis_index_page.click_download_library_link()
        # Проверяем отображения внутреннего таба "СБИС Плагин"
        self.sbis_download_report_page.plugin_tab_is_visible()
        # Кликаем по внутреннему табу "СБИС Плагин"
        self.sbis_download_report_page.click_plugin_tab()
        # Находим кнопку-ссылку скачивание "Веб-установщика"
        self.sbis_download_plugin_page.download_link_is_visible()
        # Кликаем на кнопку-ссылку скачивание "Веб-установщика"
        self.sbis_download_plugin_page.click_download_link()
        # Проверяем, что фаил скачался в дерикторию тестового проекта
        self.sbis_download_plugin_page.check_plugin_downloaded()
        # Проверяем, что размер скачанного файла соответствует 8.17 MB
        self.sbis_download_plugin_page.check_downloaded_file_size()

