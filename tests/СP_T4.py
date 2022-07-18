import time

import pytest

from base.common_test_data import CommonTestData
from pom.nav_bar import NavBar
from pom.register_form import RegisterForm


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class CP_T4:

    def execute(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        register_form = RegisterForm(driver)

        test_data = CommonTestData()
        expected_empty_name_message = test_data.get_registration_empty_form_validation_messages_by_title("name")
        expected_empty_login_message = test_data.get_registration_empty_form_validation_messages_by_title("login")
        expected_empty_password_message = test_data.get_registration_empty_form_validation_messages_by_title("password")
        expected_empty_phone_message = test_data.get_registration_empty_form_validation_messages_by_title("number")
        expected_empty_email_message = test_data.get_registration_empty_form_validation_messages_by_title("email")

        # test steps
        nav_bar.get_register_button().click()
        register_form.get_register_form_element_by_title("Зарегестрироваться").click()
        actual_empty_name_message = register_form.get_registration_form_validation_message_element_by_title("Name").text
        actual_empty_login_message = register_form.get_registration_form_validation_message_element_by_title("Login").text
        actual_empty_password_message = register_form.get_registration_form_validation_message_element_by_title("Password").text
        actual_empty_phone_message = register_form.get_registration_form_validation_message_element_by_title("PhoneNumber").text
        actual_empty_email_message = register_form.get_registration_form_validation_message_element_by_title("Email").text
        time.sleep(1)

        assert expected_empty_name_message == actual_empty_name_message \
               and expected_empty_login_message == actual_empty_login_message \
               and expected_empty_password_message == actual_empty_password_message \
               and expected_empty_phone_message == actual_empty_phone_message \
               and expected_empty_email_message == actual_empty_email_message
