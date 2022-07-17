import time

import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar
from pom.register_form import RegisterForm


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class CP_T7:

    def execute(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        register_form = RegisterForm(driver)

        test_data = CommonTestData()

        name = test_data.get_name()
        login = test_data.get_login()
        password = test_data.get_password()
        number = test_data.get_number()
        email = "username@domain."

        nav_bar.get_register_button().click()
        register_form.get_register_form_element_by_title("Name").send_keys(name)
        register_form.get_register_form_element_by_title("Login").send_keys(login)
        register_form.get_register_form_element_by_title("Password").send_keys(password)
        register_form.get_register_form_element_by_title("PhoneNumber").send_keys(number)
        register_form.get_register_form_element_by_title("Email").send_keys(email)

        register_form.get_register_form_element_by_title("Зарегестрироваться").click()
        time.sleep(1)

        actual_warning = register_form.get_registration_form_email_validation_message_element()
        expected_warning = test_data.get_registration_form_email_validation_messages_by_title("missed_second_domain")
        assert actual_warning == expected_warning
