import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from config.env_config import EnvConfig
from utils.screenshots import Screenshots
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope='session')
def config():
    return EnvConfig(Path(__file__).parent / 'config' / 'config.json')


@pytest.fixture(scope='function')
def driver(request, config):
    browser = config.get('browser', 'chrome')
    timeout = config.get('timeout', 20)
    headless = config.get('headless', False)

    if browser.lower() == 'chrome':
        options = Options()
        if headless:
            options.add_argument('--headless=new')
            options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Browser '{browser}' not supported. Only Chrome is implemented.")

    driver.maximize_window()
    driver.implicitly_wait(timeout)
    yield driver
    driver.quit()


# ✅ Correct screenshot capture hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            driver.save_screenshot(os.path.join(screenshot_dir, file_name))
            print(f"\n[INFO] Screenshot saved for failed test: {file_name}")
