from selenium.webdriver.remote.webelement import WebElement

from base.selenium_base import SeleniumBase


class HomePage(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    MAIN_AUTHORISED_NAME_PATH = "//*[@id=\"navbarCollapse\"]/div"




