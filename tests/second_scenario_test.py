from base.base_test import BaseTest
from time import sleep
import pytest


class TestSecondScenario(BaseTest):
    """Класс для тестрирования второго сценария"""
    def test_second_scenario(self):
        """Тестируем согласно второму тестовому заданию """
        self.sbis_index_page.open()
        self.sbis_index_page.click_contacts_button()
        self.sbis_contacts_page.current_region_link_is_visible()
        self.sbis_contacts_page.check_current_region_link_is_29()
        self.sbis_contacts_page.check_current_region_partners_are_visible()
        self.sbis_contacts_page.check_partners_list_exist()
        self.sbis_contacts_page.click_current_region_link()
        self.sbis_contacts_page.check_select_region_menu_is_visible()
        self.sbis_contacts_page.check_select_region_41_button_is_visible()
        self.sbis_contacts_page.click_select_region_41_button()
        self.sbis_contacts_page.check_current_region_link_is_41()
        self.sbis_contacts_page.check_current_region_partners_are_visible()
        self.sbis_contacts_page.check_partners_list_exist()
        self.sbis_contacts_page.check_current_title_is_41()
        self.sbis_contacts_page.check_url_to_be_41()

        sleep(2)