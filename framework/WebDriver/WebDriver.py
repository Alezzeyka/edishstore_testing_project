from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class WebDriver:
    xpath_selector = By.XPATH

    def driver_init(self, url: str) -> webdriver:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get(url)
        return driver

    def driver_close(self) -> None:
        webdriver.Chrome.close(self)
