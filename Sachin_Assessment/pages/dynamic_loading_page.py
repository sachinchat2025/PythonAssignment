from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.waits import Waits
import time
from selenium.webdriver.support import expected_conditions as EC

class DynamicLoadingPage:
    EXAMPLE_1 = (By.XPATH, '//a[@href="/dynamic_loading/1"]')
    EXAMPLE_2 = (By.XPATH, '//a[@href="/dynamic_loading/2"]')
    START_BTN = (By.XPATH, '//div[@id="start"]/button')
    HELLO = (By.XPATH, "//h4[text()='Hello World!']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = Waits(driver)

    def open_example_1(self):
        self.driver.find_element(*self.EXAMPLE_1).click()

    def open_example_2(self):
        self.driver.find_element(*self.EXAMPLE_2).click()

    def start_loading(self):
        self.driver.find_element(*self.START_BTN).click()

    def get_hello_text(self, timeout=60):
        """Wait until the Hello World text is visible and return it."""
        el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.HELLO)
        )
        return el.text

    def hello_is_displayed(self, timeout=60):
        """Wait until 'Hello World!' is visible and return True if displayed."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.HELLO)
            )
            return True
        except Exception:
            # Optional: take screenshot for debugging
            self.driver.save_screenshot("reports/screenshots/hello_display_failed.png")
            return False

