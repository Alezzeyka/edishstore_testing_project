import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import time


@pytest.fixture
def get_chrome_options() -> chrome_options:
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=800,600")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options) -> webdriver:
    options = get_chrome_options
    exec_path = "../Webdrivers/chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=exec_path)
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
