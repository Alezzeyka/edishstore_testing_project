from base.selenium_base import SeleniumBase


class HomePage(SeleniumBase):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver




