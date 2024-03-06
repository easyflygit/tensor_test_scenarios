from base.base_test import BaseTest


class TestFirstScenario(BaseTest):
    """Класс для тестрирования первого сценария"""
    def test_first_scenario(self):
        """Тестируем согласно первому тестовому заданию """
        # Открываем 'https://sbis.ru'
        self.sbis_index_page.open()
        # Проверяем отображение кнопки "Контакты"
        self.sbis_index_page.contact_button_is_visible()
        # Кликаем на кнопку "Контакты"
        self.sbis_index_page.click_contacts_button()
        # Находим баннер Тензор
        self.sbis_contacts_page.check_tensor_banner_is_visible()
        # Кликаем на баннер Тензор
        self.sbis_contacts_page.click_tensor_banner()
        # Переключаемся между закладками браузера на https://tensor.ru/
        self.driver.switch_to.window(self.driver.window_handles[1])
        # Проверяем что открыта страница https://tensor.ru/
        self.tensor_index_page.is_opened()
        # Прокручиваем страницу до блока "Сила в людях"
        self.tensor_index_page.scroll_to_power_in_people()
        # Проверяем, что блок "Сила в людях" отображается
        self.tensor_index_page.check_power_in_people_block_is_visible()
        # Кликаем "Подробнее" в блоке "Сила в людях"
        self.tensor_index_page.click_power_in_people_more_button()
        # Проверяем что открылась страница https://tensor.ru/about
        self.tensor_about_page.is_open()
        # Находим и прокручиваем страницу до раздела "Работаем"
        self.tensor_about_page.scroll_to_we_are_working()
        # Проверяем, что раздел "Работаем" отображается
        self.tensor_about_page.check_we_are_working_block_is_visible()
        # Проверяем, что все фотографии раздела "Работаем" отображаются
        self.tensor_about_page.check_images_are_visible()
        # Проверяем, что у всех фотографий раздела одинаковые высота и ширина
        self.tensor_about_page.check_images_size_is_equal()




