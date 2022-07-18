import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import logging
import os


@pytest.fixture
def get_chrome_options() -> ChromeOptions:
    options = ChromeOptions()
    options.add_argument('chrome')
    options.add_argument("headless")
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options) -> webdriver:
    services = Service(ChromeDriverManager().install())
    options = get_chrome_options
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    os.environ['WDM_LOG'] = "false"
    driver = webdriver.Chrome(options=options, service=services)
    driver.maximize_window()
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver: webdriver):
    driver = get_webdriver
    url = "https://localhost:44304"
    request.cls.driver = driver
    driver.get(url)
    time.sleep(5)

    yield driver
    driver.close()
