import time

import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class Test_CP_T2:

    def test(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        login_form = LoginForm(driver)

        test_data = CommonTestData()
        login = test_data.get_login(rnd=False)
        password = test_data.get_password(rnd=False)

        nav_bar.get_login_button().click()
        login_form.get_login_form_element_by_title("login").send_keys(login)
        login_form.get_login_form_element_by_title("password").send_keys(password)
        login_form.get_login_form_element_by_title("Войти").click()
        time.sleep(1)

        actual_name = nav_bar.get_authorized_user_name().text[14:]
        expected_name = test_data.get_name(rnd=False)
        assert expected_name == actual_name
