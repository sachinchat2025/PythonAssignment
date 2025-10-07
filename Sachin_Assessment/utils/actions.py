from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Actions:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def hover(self, element):
        self.action.move_to_element(element).perform()

    def double_click(self, element):
        self.action.double_click(element).perform()

    def send_keys(self, element, keys):
        element.clear()
        element.send_keys(keys)

    def press_enter(self):
        self.action.send_keys(Keys.ENTER).perform()
