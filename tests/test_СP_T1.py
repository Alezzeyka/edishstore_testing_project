import time

import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar
from pom.register_form import RegisterForm


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class Test_CP_T1:

    def test(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        register_form = RegisterForm(driver)
        login_form = LoginForm(driver)

        test_data = CommonTestData()

        name = test_data.get_name()
        login = test_data.get_login()
        password = test_data.get_password()
        number = test_data.get_number()
        email = test_data.get_email()

        nav_bar.get_register_button().click()
        register_form.get_register_form_element_by_title("Name").send_keys(name)
        register_form.get_register_form_element_by_title("Login").send_keys(login)
        register_form.get_register_form_element_by_title("Password").send_keys(password)
        register_form.get_register_form_element_by_title("PhoneNumber").send_keys(number)
        register_form.get_register_form_element_by_title("Email").send_keys(email)
        time.sleep(1)
        register_form.get_register_form_element_by_title("Зарегестрироваться").click()

        nav_bar.get_login_button().click()
        login_form.get_login_form_element_by_title("login").send_keys(login)
        login_form.get_login_form_element_by_title("password").send_keys(password)
        time.sleep(1)
        login_form.get_login_form_element_by_title("Войти").click()

        actual_name = nav_bar.get_authorized_user_name().text[14:]
        expected_name = name
        assert expected_name == actual_name
