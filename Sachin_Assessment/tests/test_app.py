import pytest
import logging
from pages.home_page import HomePage
from pages.challenging_dom_page import ChallengingDomPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.shifting_content_page import ShiftingContentPage

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Optional: log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(console_handler)


class TestTheInternet:

    @pytest.mark.smoke
    def test_challenging_dom_buttons(self, driver, config):
        base_url = config.get('base_url')
        home = HomePage(driver, timeout=config.get('timeout'))
        logger.info("Opening base URL: %s", base_url)
        home.open(base_url)

        logger.info("Navigating to Challenging DOM page")
        home.go_to_challenging_dom()
        page = ChallengingDomPage(driver)

        logger.info("Clicking primary button")
        page.click_primary()
        assert page.has_answer_script(), "Answer script should be present after clicking primary button"

        logger.info("Clicking alert button")
        page.click_alert()
        assert page.has_answer_script(), "Answer script should be present after clicking alert button"

        logger.info("Clicking success button")
        page.click_success()
        assert page.has_answer_script(), "Answer script should be present after clicking success button"

    def test_dynamic_loading_examples(self, driver, config):
        base_url = config.get('base_url')
        home = HomePage(driver, timeout=config.get('timeout'))
        logger.info("Opening base URL: %s", base_url)
        home.open(base_url)

        logger.info("Navigating to Dynamic Loading page")
        home.go_to_dynamic_loading()
        dyn = DynamicLoadingPage(driver)

        # Example 1
        logger.info("Opening Example 1")
        dyn.open_example_1()
        dyn.start_loading()
        text = dyn.get_hello_text()
        logger.info("Example 1 text: %s", text)
        assert text == 'Hello World!', f"Expected 'Hello World!' got '{text}'"
        driver.back()

        # Example 2
        logger.info("Opening Example 2")
        dyn.open_example_2()
        dyn.start_loading()
        displayed = dyn.hello_is_displayed()
        logger.info("Example 2 hello displayed: %s", displayed)
        assert displayed

    @pytest.mark.regression
    def test_shifting_content(self, driver, config):
        base_url = config.get("base_url")
        home = HomePage(driver)
        logger.info("Opening base URL: %s", base_url)
        home.open(base_url)

        logger.info("Navigating to Shifting Content page")
        home.go_to_shifting_content()
        sc = ShiftingContentPage(driver)

        # Menu
        logger.info("Clicking Menu link")
        sc.go_to_menu()
        driver.back()

        # Image
        logger.info("Clicking Image link")
        sc.go_to_image()
        image_displayed = sc.image_is_displayed()
        logger.info("Image displayed: %s", image_displayed)
        assert image_displayed
        driver.back()

        # List
        logger.info("Clicking List link")
        sc.go_to_list()
        list_text = sc.get_list_text()
        logger.info("List text: %s", list_text)
        print(list_text)
        driver.back()
