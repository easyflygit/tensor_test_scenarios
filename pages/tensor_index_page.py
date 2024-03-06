from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TensorIndexPage(BasePage):
    """Класс для страницы 'https://tensor.ru'"""
    PAGE_URL = Links.TENSOR_INDEX

    POWER_IN_PEOPLE_BLOCK = ("xpath",
                             "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']")
    POWER_IN_PEOPLE_MORE_BUTTON = ("xpath", '(//a[@href="/about"])[2]')

    def check_power_in_people_block_is_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.POWER_IN_PEOPLE_BLOCK))

    def click_power_in_people_more_button(self):
        self.wait.until(EC.element_to_be_clickable(self.POWER_IN_PEOPLE_MORE_BUTTON)).click()

    def scroll_to_power_in_people(self):
        iframe = self.wait.until(EC.visibility_of_element_located(self.POWER_IN_PEOPLE_BLOCK))
        ActionChains(self.driver) \
            .scroll_to_element(iframe) \
            .perform()