from typing import List, Dict
from selenium.webdriver.remote.webelement import WebElement
from base.selenium_base import SeleniumBase
from base.utils import Utils


class NavBar(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    __XPATH_NAV = "//*[@id=\"navbarCollapse\"]/ul{}"
    __NAV_LINK_TEXT = "Главная,Корзина,Тарелки,Чашки,Стаканы"
    __LOGIN_BUTTON = "//button[text()=\"Войти\"]"
    __REGISTER_BUTTON = "//button[text()=\"Регистрация\"]"
    __XPATH_AUTHORIZED_USER_NAME = "//*[@id=\"navbarCollapse\"]/div"
    __XPATH_AUTHORIZED_USER_PERSONAL_INFO = "//*[@id=\"navbarCollapse\"]/a[1]"
    __XPATH_AUTHORIZED_USER_LOGOUT = "//*[@id=\"navbarCollapse\"]/a[2]"

    def __get_nav_categories_xpath_dict(self) -> dict:
        categories_names = ("Тарелки", "Чашки", "Стаканы")
        nav_categories_xpath = {}.fromkeys(categories_names)
        for category_name in categories_names:
            nav_categories_xpath[category_name] = self.__XPATH_NAV.format(categories_names.index(category_name)+1)
        return nav_categories_xpath

    def __get_nav_category_xpath(self, name: str) -> str:
        category_xpath_dict = self.__get_nav_categories_xpath_dict()
        return category_xpath_dict.get(name.lower())

    def get_nav_link_by_name(self, name: str) -> WebElement:
        return self.is_visible("xpath", self.__get_nav_category_xpath(name), f"{name} navbar category")

    def get_login_button(self) -> WebElement:
        return self.is_visible("xpath", self.__LOGIN_BUTTON, "Login Button")

    def get_register_button(self) -> WebElement:
        return self.is_visible("xpath", self.__REGISTER_BUTTON, "Register Button")

    def get_authorized_user_name(self) -> WebElement:
        return self.is_visible("xpath", self.__XPATH_AUTHORIZED_USER_NAME, "Authorised user name")

    def get_authorized_personal_info(self) -> WebElement:
        return self.is_visible("xpath", self.__XPATH_AUTHORIZED_USER_PERSONAL_INFO, "Authorised user Personal Info "
                                                                                    "button")

    def get_authorized_logout(self) -> WebElement:
        return self.is_visible("xpath", self.__XPATH_AUTHORIZED_USER_LOGOUT, "Authorised user Logout Button")
