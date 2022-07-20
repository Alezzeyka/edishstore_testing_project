from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class SeleniumBase:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {"xpath": By.XPATH,
                    "css": By.CSS_SELECTOR,
                    'class_name': By.CLASS_NAME,
                    "id": By.ID,
                    "link_text": By.LINK_TEXT,
                    "partial_link_text": By.PARTIAL_LINK_TEXT,
                    "name": By.NAME,
                    "tag_name": By.TAG_NAME
                    }

        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)
