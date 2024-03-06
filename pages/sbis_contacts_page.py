from selenium.common import ElementNotInteractableException

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class SbisContactsPage(BasePage):
    """Класс для страницы 'https://sbis.ru/contacts'"""
    PAGE_URL = Links.SBIS_CONTACTS_PAGE

    TENSOR_BANNER = ("xpath", "(//img[@alt='Разработчик системы СБИС — компания «Тензор»'])[1]")
    REGION_LINK = ("xpath", '(//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"])[1]')
    CURRENT_REGION_29 = ("xpath", '(//span[text()="Архангельская обл."])[1]')
    PARTNERS = ("xpath", '//div[@class="sbisru-Contacts-List__col ws-flex-shrink-1 ws-flex-grow-1"]')
    PARTNERS_LIST = ("xpath", '(//div[@data-qa="list"])[1]')
    REGION_SELECT_MENU = ("xpath", '//div[@name="dialog"]')
    REGION_41_SELECTOR = ("xpath", '//span[@title="Камчатский край"]')

    def check_tensor_banner_is_visible(self):
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER))

    def click_tensor_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.TENSOR_BANNER)).click()

    def current_region_link_is_visible(self):
        return self.wait.until(EC.element_to_be_clickable(self.REGION_LINK))

    def click_current_region_link(self):
        self.current_region_link_is_visible().click()

    def check_current_region_link_is_29(self):
        self.wait.until(EC.text_to_be_present_in_element(self.REGION_LINK, "Архангельская обл."))

    def check_current_region_partners_are_visible(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.PARTNERS_LIST))

    def check_partners_list_exist(self):
        partners_list = []
        partners = self.check_current_region_partners_are_visible()
        for partner in partners:
            try:
                partners_list.append(partner.text)
            except ElementNotInteractableException:
                print("No partners available")
        return print(str(partners_list).replace('\\n', ',\n'))

    def check_select_region_menu_is_visible(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.REGION_SELECT_MENU))

    def check_select_region_41_button_is_visible(self):
        self.wait.until(EC.element_to_be_clickable(self.REGION_41_SELECTOR))

    def click_select_region_41_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REGION_41_SELECTOR)).click()

    def check_current_region_link_is_41(self):
        self.wait.until(EC.text_to_be_present_in_element(self.REGION_LINK, "Камчатский край"))

    def check_current_title_is_41(self):
        self.wait.until(EC.title_contains("Камчатский край"))

    def check_url_to_be_41(self):
        self.wait.until(EC.url_to_be("https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"))


