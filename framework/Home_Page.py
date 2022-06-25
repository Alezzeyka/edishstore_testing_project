from framework import Common_Page


class Home_Page(Common_Page):
    LOGIN_PATH = "//input[@name=\"login\"]"
    PASSWORD_PATH = "//input[@name=\"password\"]"
    BUTTON_PATH = "//input[@value=\"Войти\"]"
