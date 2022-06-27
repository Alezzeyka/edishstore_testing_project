import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


@pytest.fixture
def get_chrome_options() -> chrome_options:
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument("--start-maximized")
    # options.add_argument("--window-size=800,600")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options) -> webdriver:
    services = Service(ChromeDriverManager().install())
    options = get_chrome_options
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
