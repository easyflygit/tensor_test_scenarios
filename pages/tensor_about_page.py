from selenium.common import ElementNotInteractableException

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TensorAboutPage(BasePage):
    """Класс для страницы 'https://tensor.ru/about'"""
    PAGE_URL = Links.TENSOR_ABOUT_PAGE

    WE_ARE_WORKING_BLOCK = ("xpath",
                            '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')
    BLOCK_IMAGES = ("xpath",
                    '//div[@class="tensor_ru-About__block3-image-filter"]')

    def is_open(self):
        url = self.driver.current_url
        assert url == "https://tensor.ru/about", "URL isn't match"

    def check_we_are_working_block_is_visible(self):
        self.wait.until(EC.presence_of_element_located(self.WE_ARE_WORKING_BLOCK))

    def scroll_to_we_are_working(self):
        iframe = self.wait.until(EC.visibility_of_element_located(self.WE_ARE_WORKING_BLOCK))
        ActionChains(self.driver) \
            .scroll_to_element(iframe) \
            .perform()

    def check_images_are_visible(self):
        self.wait.until(EC.presence_of_all_elements_located(self.BLOCK_IMAGES))

    def check_images_size_is_equal(self):
        images = self.wait.until(EC.presence_of_all_elements_located(self.BLOCK_IMAGES))
        # Print size of all the images
        for image in images:
            try:
                print(image.size)
            except ElementNotInteractableException:
                print("image could be hidden")

        assert images[0].size == images[1].size and images[2].size and images[3].size


