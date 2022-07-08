from selenium.webdriver.remote.webelement import WebElement

from base.selenium_base import SeleniumBase


class LoginForm(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    __LOGIN_FORM_FIELD_PATH = "//input[@name=\"{}\"]"
    __LOGIN_FORM_BUTTON_PATH = "//input[@value=\"Войти\"]"
    __WRONG_LOGIN_DETAILS_MESSAGE_XPATH = "//div[@class=\"alert alert-danger\"]"

    def __get_login_form_elements_xpath_dict(self) -> dict:
        elements_names = ("login", "password", "Войти")
        nav_categories_xpath = {}.fromkeys(elements_names)
        for element_name in elements_names:
            if element_name != "Войти":
                nav_categories_xpath[element_name] = self.__LOGIN_FORM_FIELD_PATH.format(element_name)
            else:
                nav_categories_xpath[element_name] = self.__LOGIN_FORM_BUTTON_PATH
        return nav_categories_xpath

    def __get_login_form_element_xpath(self, name: str) -> str:
        category_xpath_dict = self.__get_login_form_elements_xpath_dict()
        return category_xpath_dict.get(name)

    def get_login_form_element_by_title(self, title: str) -> WebElement:
        return self.is_visible("xpath", self.__get_login_form_element_xpath(title), f"Login form {title} element")

    def get_wrong_login_details_message(self):
        return self.is_visible("xpath", self.__WRONG_LOGIN_DETAILS_MESSAGE_XPATH, f"Wrong login details message "
                                                                                    f"element")
