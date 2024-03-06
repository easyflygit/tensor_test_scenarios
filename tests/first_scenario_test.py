import pytest
from base.base_test import BaseTest


class TestFirstScenario(BaseTest):
    """Класс для тестрирования первого сценария"""
    def test_first_scenario(self):
        """Тестируем согласно первому тестовому заданию """
        self.sbis_index_page.open()
        self.sbis_index_page.contact_button_is_visible()
        self.sbis_index_page.click_contacts_button()
        self.sbis_contacts_page.check_tensor_banner_is_visible()
        self.sbis_contacts_page.click_tensor_banner()
        # Переключаемся на закладку "https://tensor.ru"
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.tensor_index_page.is_opened()
        self.tensor_index_page.scroll_to_power_in_people()
        self.tensor_index_page.check_power_in_people_block_is_visible()
        self.tensor_index_page.click_power_in_people_more_button()
        self.tensor_about_page.is_open()
        self.tensor_about_page.scroll_to_we_are_working()
        self.tensor_about_page.check_we_are_working_block_is_visible()
        self.tensor_about_page.check_images_are_visible()
        self.tensor_about_page.check_images_size_is_equal()




