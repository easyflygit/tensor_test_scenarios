from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class SbisIndexPage(BasePage):
    """Класс для страницы 'https://sbis.ru'"""
    PAGE_URL = Links.SBIS_INDEX

    CONTACTS_BUTTON = ("xpath", '(//a[@href="/contacts"])[1]')
    FOOTER = ("xpath", '//div[@class="sbisru-Footer sbisru-Footer__scheme--default"]')
    DOWNLOAD_LIBRARY_LINK = ("xpath", '//a[@href="/download"]')

    def contact_button_is_visible(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACTS_BUTTON))

    def click_contacts_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACTS_BUTTON)).click()

    def scroll_to_footer(self):
        iframe = self.wait.until(EC.visibility_of_element_located(self.FOOTER))
        ActionChains(self.driver) \
            .scroll_to_element(iframe) \
            .perform()

    def download_library_link_is_visible(self):
        self.wait.until(EC.visibility_of_element_located(self.DOWNLOAD_LIBRARY_LINK))

    def click_download_library_link(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_LIBRARY_LINK)).click()



