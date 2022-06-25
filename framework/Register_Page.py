from framework.Common_Page import Common_Page


class Register_Page(Common_Page):
    NAME_PATH = "//*[@id=\"Name\"]"
    LOGIN_PATH = "//*[@id=\"Login\"]"
    PASSWORD_PATH = "//*[@id=\"Password\"]"
    EMAIL_PATH = "//*[@id=\"Email\"]"
    PHONE_PATH = "//*[@id=\"PhoneNumber\"]"
    BUTTON_PATH = "/html/body/div/div/form/input[1]"
