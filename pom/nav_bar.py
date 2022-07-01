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
    __LOGIN_BUTTON = "//*[@id=\"navbarCollapse\"]/form[2]/button"
    __XPATH_AUTHORISED_USER_SIGN = "//*[@id=\"navbarCollapse\"]/div"

    def __get_nav_categories_xpath_dict(self) -> dict:
        categories_names = ("Тарелки", "Чашки", "Стаканы")
        nav_categories_xpath = {}.fromkeys(categories_names)
        for category_name in categories_names:
            nav_categories_xpath[category_name.lower()] = self.__XPATH_NAV.format(categories_names.index(category_name)+1)
        return nav_categories_xpath

    def __get_nav_category_xpath(self, name: str) -> str:
        category_xpath_dict = self.__get_nav_categories_xpath_dict()
        return category_xpath_dict.get(name.lower())

    def get_nav_link_by_name(self, name: str) -> WebElement:
        return self.is_visible("xpath", self.__get_nav_category_xpath(name), f"{name} navbar category")

    def get_login_button(self) -> WebElement:
        return self.is_visible("xpath", self.__LOGIN_BUTTON, "Login Button")

    def get_authorised_user_sign(self) -> WebElement:
        return self.is_visible("xpath", self.__XPATH_AUTHORISED_USER_SIGN, "Authorised user greetings message")
