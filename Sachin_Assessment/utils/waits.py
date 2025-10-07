from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

class Waits:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def wait_for_element_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_and_click(self, by, locator):
        el = self.wait_for_element_visible(by, locator)
        el.click()
        return el

    def wait_for_text(self, by, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element((by, locator), text))

    def wait_for_element_to_be_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def wait_for_element_to_be_displayed(self, by, locator, timeout=30):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                el = self.driver.find_element(by, locator)
                if el.is_displayed():
                    return el
            except:
                pass
            time.sleep(0.5)
        raise TimeoutException(f"Element ({by}, {locator}) not displayed within {timeout}s")

