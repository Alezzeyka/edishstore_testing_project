from selenium.webdriver.remote.webelement import WebElement

from base.selenium_base import SeleniumBase


class RegisterForm(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    __ELEMENT_FIELD_XPATH = "//*[@id=\"{}\"]"
    __BUTTON_XPATH = "//input[@type=\"submit\"]"
    __REGISTER_VALIDATION_MESSAGES_XPATH = "//*[@data-valmsg-for=\"{}\"]"

    def __get_register_form_elements_dict(self) -> dict:
        names_list = ("Name", "Login", "Password", "Email", "PhoneNumber", "Зарегестрироваться")
        register_form_elements_dict = dict.fromkeys(names_list)
        for element in register_form_elements_dict:
            if element != "Зарегестрироваться":
                register_form_elements_dict[element] = self.__ELEMENT_FIELD_XPATH.format(element)
            else:
                register_form_elements_dict[element] = self.__BUTTON_XPATH
        return register_form_elements_dict

    def __get_register_validation_messages_dict(self) -> dict:
        names_list = ("Name", "Login", "Password", "Email", "PhoneNumber")
        validating_messages_dict = dict.fromkeys(names_list)
        for element in validating_messages_dict:
            validating_messages_dict[element] = self.__REGISTER_VALIDATION_MESSAGES_XPATH.format(element)
        return validating_messages_dict

    def __get_register_form_xpath_by_title(self, title: str) -> str:
        register_form_elements_dict = self.__get_register_form_elements_dict()
        return register_form_elements_dict[title]

    def get_register_form_element_by_title(self, title: str) -> WebElement:
        return self.is_visible("xpath", self.__get_register_form_xpath_by_title(title), f"{title} field path")

    def __get_register_validating_messages_xpath_by_title(self, title: str) -> str:
        register_validating_messages_dict = self.__get_register_validation_messages_dict()
        return register_validating_messages_dict[title]

    def get_register_validation_message_element_by_title(self, title: str) -> WebElement:
        return self.is_visible("xpath", self.__get_register_validating_messages_xpath_by_title(title), f"{title} validating message path")
