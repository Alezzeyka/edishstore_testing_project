import time

from Test_cases.Common_Test import Common_Test
from WebDriver import WebDriver
from pom.Common_Page import Common_Page
from pom.Login_Page import Login_Page


class CP_T2(Common_Test):
    def __init__(self):
        self.name = super().name
        self.login = super().login[:5]
        self.password = super().password
        self.email = super().email
        self.phone = super().phone
        self.__uri = "/User/LoginPage"
        self.url = super().url + self.__uri

    def execute(self, driver: WebDriver):
        driver = driver.driver_init(self.url)

        try:
            login_page = Login_Page()
            common_page = Common_Page()

            time.sleep(1)

            driver.find_element(WebDriver.xpath_selector, login_page.LOGIN_PATH).send_keys(self.login)
            driver.find_element(WebDriver.xpath_selector, login_page.PASSWORD_PATH).send_keys(self.password)
            driver.find_element(WebDriver.xpath_selector, login_page.BUTTON_PATH).click()

            time.sleep(1)

            actual_name = driver.find_element(WebDriver.xpath_selector, common_page.MAIN_AUTHORISED_NAME_PATH).text[14:]

            if self.name == actual_name:
                print("CP-T2: All OK")
            else:
                print("CP-T2: Something not OK")
        except ValueError:
            print("CP-T2: Something go wrong")
