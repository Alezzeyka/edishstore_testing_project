from framework.Common_Page import Common_Page


class Login_Page(Common_Page):
    LOGIN_PATH = "//input[@name=\"login\"]"
    PASSWORD_PATH = "//input[@name=\"password\"]"
    BUTTON_PATH = "//input[@value=\"Войти\"]"
