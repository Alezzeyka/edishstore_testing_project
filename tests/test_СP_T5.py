import pytest

from base.common_test_data import CommonTestData
from pom.login_form import LoginForm
from pom.nav_bar import NavBar


@pytest.mark.regression
@pytest.mark.usefixtures("setup")
class Test_CP_T5:

    def test(self):
        driver = self.driver
        nav_bar = NavBar(driver)
        login_form = LoginForm(driver)

        test_data = CommonTestData()

        # test steps
        nav_bar.get_login_button().click()
        login_form.get_login_form_element_by_title("Войти").click()

        actual_info_message = login_form.get_wrong_login_details_message().text
        expected_info_message = test_data.get_information_message_text_by_title("wrong_login_details")
        assert actual_info_message == expected_info_message
