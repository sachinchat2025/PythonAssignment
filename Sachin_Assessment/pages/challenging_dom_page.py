from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChallengingDomPage(BasePage):
    BUTTON = (By.XPATH, '//a[@class="button"]')
    BUTTON_ALERT = (By.XPATH, '//a[@class="button alert"]')
    BUTTON_SUCCESS = (By.XPATH, '//a[@class="button success"]')
    SCRIPT_ANSWER = (By.XPATH, "//script[contains(text(),'Answer:')]")

    def click_primary(self):
        self.click(*self.BUTTON)

    def click_alert(self):
        self.click(*self.BUTTON_ALERT)

    def click_success(self):
        self.click(*self.BUTTON_SUCCESS)

    def has_answer_script(self):
        scripts = self.driver.find_elements(By.XPATH, "//script[contains(text(),'Answer:')]")
        print("sachin")
        return len(scripts) > 0

