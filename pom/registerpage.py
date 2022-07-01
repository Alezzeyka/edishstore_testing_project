from base.selenium_base import SeleniumBase


class RegisterPage(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    NAME_PATH = "//*[@id=\"Name\"]"
    LOGIN_PATH = "//*[@id=\"Login\"]"
    PASSWORD_PATH = "//*[@id=\"Password\"]"
    EMAIL_PATH = "//*[@id=\"Email\"]"
    PHONE_PATH = "//*[@id=\"PhoneNumber\"]"
    BUTTON_PATH = "/html/body/div/div/form/input[1]"
