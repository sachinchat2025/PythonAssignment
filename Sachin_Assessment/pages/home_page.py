from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    CHALLENGING_DOM = (By.XPATH, '//a[@href="/challenging_dom"]')
    DYNAMIC_LOADING = (By.XPATH, '//a[@href="/dynamic_loading"]')
    SHIFTING_CONTENT = (By.XPATH, '//a[@href="/shifting_content"]')

    def go_to_challenging_dom(self):
        self.click(*self.CHALLENGING_DOM)

    def go_to_dynamic_loading(self):
        self.click(*self.DYNAMIC_LOADING)

    def go_to_shifting_content(self):
        self.click(*self.SHIFTING_CONTENT)
