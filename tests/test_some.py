import time

import pytest
from selenium import webdriver
from pom.nav_bar import NavBar


@pytest.mark.usefixtures("setup")
class Test:

    def test_nav_category_links(self):
        nav_bar = NavBar(self.driver)
        actual_links = nav_bar.get_nav_links_text()
        expected_links = NavBar.NAV_LINK_TEXT
        assert actual_links == expected_links, "Validating nav links test"
        nav_bar.get_nav_link_by_name("Тарелки").click()
        time.sleep(5)
