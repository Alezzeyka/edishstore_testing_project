import time

import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar
from pom.registerpage import RegisterForm


@pytest.mark.usefixtures("setup")
class Test_CP_T1:

    def test_nav_category_links(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        register_form = RegisterForm(driver)
        login_form = LoginForm(driver)

        test_data = CommonTestData()

        name = test_data.get_test_data_by_title("name")
        login = test_data.get_test_data_by_title("login")
        password = test_data.get_test_data_by_title("password")
        email = test_data.get_test_data_by_title("email")
        number = test_data.get_test_data_by_title("number")

        nav_bar.get_register_button().click()
        register_form.get_register_form_element_by_name("name")
        register_form.get_register_form_element_by_name("login")
        register_form.get_register_form_element_by_name("password")
        register_form.get_register_form_element_by_name("re-password")
        register_form.get_register_form_element_by_name("number")
        register_form.get_register_form_element_by_name("email")
        register_form.get_register_button().click()

        nav_bar.get_login_button().click()
        login_form.get_login_form_element_by_name("login").send_keys(login)
        login_form.get_login_form_element_by_name("password").send_keys(password)
        login_form.get_login_form_element_by_name("Войти").click()
        time.sleep(1)

        actual_name = nav_bar.get_authorised_user_sign().text[14:]
        expected_name = name
        assert expected_name == actual_name
