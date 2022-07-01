from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.selenium_base import SeleniumBase


class LoginForm(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    __LOGIN_FORM_FIELD_PATH = "//input[@name=\"{}\"]"
    __LOGIN_FORM_BUTTON_PATH = "//input[@value=\"Войти\"]"

    def __get_login_form_elements_xpath_dict(self) -> dict:
        elements_names = ("login", "password", "Войти")
        nav_categories_xpath = {}.fromkeys(elements_names)
        for element_name in elements_names:
            if element_name != "Войти":
                nav_categories_xpath[element_name.lower()] = self.__LOGIN_FORM_FIELD_PATH.format(element_name)
            else:
                nav_categories_xpath[element_name.lower()] = self.__LOGIN_FORM_BUTTON_PATH
        return nav_categories_xpath

    def __get_login_form_element_xpath(self, name: str) -> str:
        name = name.lower()
        category_xpath_dict = self.__get_login_form_elements_xpath_dict()
        return category_xpath_dict.get(name.lower())

    def get_login_form_element_by_name(self, name: str) -> WebElement:
        name = name.lower()
        return self.is_visible("xpath", self.__get_login_form_element_xpath(name), f"Login form {name} element")
