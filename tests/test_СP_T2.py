import time

import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar


@pytest.mark.usefixtures("setup")
class Test_CP_T2:

    def test_nav_category_links(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        login_form = LoginForm(driver)

        test_data = CommonTestData()
        login = test_data.get_test_data_by_title("login")
        password = test_data.get_test_data_by_title("password")

        nav_bar.get_login_button().click()
        login_form.get_login_form_element_by_title("login").send_keys(login)
        login_form.get_login_form_element_by_title("password").send_keys(password)
        login_form.get_login_form_element_by_title("Войти").click()
        time.sleep(1)

        actual_name = nav_bar.get_authorised_user_sign().text[14:]
        expected_name = test_data.get_test_data_by_title("name")
        assert expected_name == actual_name
