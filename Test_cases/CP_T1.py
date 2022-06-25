import time

from framework.Test_Structures.Common_Test import Common_Test
from framework.WebDriver.WebDriver import WebDriver
from framework.Common_Page import Common_Page
from framework.Register_Page import Register_Page
from framework.Login_Page import Login_Page


class CP_T1(Common_Test):
    def __init__(self):
        self.name = super().name
        self.login = super().login
        self.password = super().password
        self.email = super().email
        self.phone = super().phone
        self.__uri = "/User/Register"
        self.url = super().url + self.__uri

    def execute(self, driver: WebDriver):
        driver = driver.driver_init(self.url)

        try:
            register_page = Register_Page()
            login_page = Login_Page()
            common_page = Common_Page()

            time.sleep(1)

            driver.find_element(WebDriver.xpath_selector, register_page.NAME_PATH).send_keys(self.name)
            driver.find_element(WebDriver.xpath_selector, register_page.LOGIN_PATH).send_keys(self.login)
            driver.find_element(WebDriver.xpath_selector, register_page.PASSWORD_PATH).send_keys(self.password)
            driver.find_element(WebDriver.xpath_selector, register_page.EMAIL_PATH).send_keys(self.email)
            driver.find_element(WebDriver.xpath_selector, register_page.PHONE_PATH).send_keys(self.phone)
            driver.find_element(WebDriver.xpath_selector, register_page.BUTTON_PATH).click()

            time.sleep(1)

            driver.find_element(WebDriver.xpath_selector, login_page.LOGIN_PATH).send_keys(self.login)
            driver.find_element(WebDriver.xpath_selector, login_page.PASSWORD_PATH).send_keys(self.password)
            driver.find_element(WebDriver.xpath_selector, login_page.BUTTON_PATH).click()

            time.sleep(1)

            actual_name = driver.find_element(WebDriver.xpath_selector, common_page.MAIN_AUTHORISED_NAME_PATH).text[14:]

            if self.name == actual_name:
                print("CP-T1: All OK")
            else:
                print("CP-T1: Something not OK")

        except ValueError:
            print("CP-T1: Something go wrong")
