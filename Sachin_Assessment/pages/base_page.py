from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.waits import Waits
from utils.actions import Actions


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = Waits(driver, timeout)
        self.actions = Actions(driver)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.wait_for_element(by, locator)

    def click(self, by, locator):
        return self.wait.wait_and_click(by, locator)

    def is_displayed(self, by, locator):
        try:
            return self.wait.wait_for_element_visible(by, locator).is_displayed()
        except Exception:
            return False

    def screenshot(self, file_path: str):
        return self.driver.save_screenshot(file_path)
