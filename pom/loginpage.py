from selenium.webdriver.remote.webelement import WebElement

from base.selenium_base import SeleniumBase


class LoginPage(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    __LOGIN_PATH = "//input[@name=\"login\"]"
    __PASSWORD_PATH = "//input[@name=\"password\"]"
    __BUTTON_PATH = "//input[@value=\"Войти\"]"