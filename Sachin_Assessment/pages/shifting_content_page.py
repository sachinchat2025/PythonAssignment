from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.waits import Waits

class ShiftingContentPage(BasePage):
    MENU_LINK = (By.XPATH, '//a[@href="/shifting_content/menu"]')
    IMAGE_LINK = (By.XPATH, '//a[@href="/shifting_content/image"]')
    IMAGE = (By.XPATH, '//img[@class="shift"]')
    LIST_LINK = (By.XPATH, '//a[@href="/shifting_content/list"]')
    LIST_TEXT = (By.XPATH, "//div[@class='large-6 columns large-centered']")

    def __init__(self, driver, timeout=20):
        super().__init__(driver)
        self.wait = Waits(driver, timeout)

    def go_to_menu(self):
        self.driver.find_element(*self.MENU_LINK).click()

    def go_to_image(self):
        self.driver.find_element(*self.IMAGE_LINK).click()

    def image_is_displayed(self):
        return self.driver.find_element(*self.IMAGE).is_displayed()

    def go_to_list(self):
        self.driver.find_element(*self.LIST_LINK).click()

    def get_list_text(self):
        return self.driver.find_element(*self.LIST_TEXT).text
