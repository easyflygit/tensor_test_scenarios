from base.base_test import BaseTest
from time import sleep


class TestSecondScenario(BaseTest):
    """Класс для тестрирования второго сценария"""
    def test_second_scenario(self):
        """Тестируем согласно второму тестовому заданию """
        # Открываем 'https://sbis.ru'
        self.sbis_index_page.open()
        # Кликаем на кнопку "Контакты"
        self.sbis_index_page.click_contacts_button()
        # Находим ссылку отображения региона
        self.sbis_contacts_page.current_region_link_is_visible()
        # Проверяем, что определился наш регион(в примере Архангельская обл.)
        self.sbis_contacts_page.check_current_region_link_is_29()
        # Проверяем, что список партнеров отображается (Архангельск)
        self.sbis_contacts_page.check_current_region_partners_are_visible()
        # Проверяем, что список с партнерами существует
        self.sbis_contacts_page.check_partners_list_exist()
        # Кликаем на ссылку отображения региона
        self.sbis_contacts_page.click_current_region_link()
        # Проверяем, что меню выбора региона отображается
        self.sbis_contacts_page.check_select_region_menu_is_visible()
        # Проверяем, что кнопка "41 Камчатский край" отображается
        self.sbis_contacts_page.check_select_region_41_button_is_visible()
        # Кликаем на кнопку "41 Камчатский край"
        self.sbis_contacts_page.click_select_region_41_button()
        # Проверяем, что определился регион "Камчатский край"
        self.sbis_contacts_page.check_current_region_link_is_41()
        # Проверяем, что список партнеров отображается (Петропавлоск-Камчатский)
        self.sbis_contacts_page.check_current_region_partners_are_visible()
        # Проверяем, что список с партнерами существует
        self.sbis_contacts_page.check_partners_list_exist()
        # Проверяем, что Title содержит информацию выбранного региона
        self.sbis_contacts_page.check_current_title_is_41()
        # Проверяем, что URL содержит информацию выбранного региона
        self.sbis_contacts_page.check_url_to_be_41()

        sleep(2)