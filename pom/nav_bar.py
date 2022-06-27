from typing import List, Dict
from selenium.webdriver.remote.webelement import WebElement
from base.selenium_base import SeleniumBase
from base.utils import Utils


class NavBar(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    __XPATH_NAV = "//*[@id=\"navbarCollapse\"]/ul"
    NAV_LINK_TEXT = "Главная,Корзина,Тарелки,Чашки,Стаканы"

    def __get_nav_categories_xpath_dict(self) -> dict:
        categories_names = ("Тарелки", "Чашки", "Стаканы")
        nav_categories_xpath = {}.fromkeys(categories_names)
        for category_name in categories_names:
            nav_categories_xpath[category_name.lower()] = self.__XPATH_NAV + f"[{categories_names.index(category_name)+1}]"
        return nav_categories_xpath

    def get_nav_category_xpath(self, name: str) -> str:
        category_xpath_dict = self.__get_nav_categories_xpath_dict()
        return category_xpath_dict.get(name.lower())

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible("xpath", self.__XPATH_NAV, "Category Links Navbar")

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_web_elements(nav_links)
        return Utils.join_strings(nav_links_text, enters=True)

    def get_nav_link_by_name(self, name: str) -> WebElement:
        return self.is_visible("xpath", self.get_nav_category_xpath(name), f"{name} navbar category")