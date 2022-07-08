import time

import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar


@pytest.mark.usefixtures("setup")
class Test_CP_T2:

    def test(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        login_form = LoginForm(driver)

        test_data = CommonTestData()

        login = test_data.get_login(rnd=False)
        password = test_data.get_password(rnd=False)

        # preconditions
        nav_bar.get_login_button().click()
        login_form.get_login_form_element_by_title("login").send_keys(login)
        login_form.get_login_form_element_by_title("password").send_keys(password)
        login_form.get_login_form_element_by_title("Войти").click()

        # test steps
        nav_bar.get_authorized_logout().click()
        actual_login_button_text = nav_bar.get_login_button().text
        expected_login_button_text = test_data.get_login_text()
        assert actual_login_button_text == expected_login_button_text
