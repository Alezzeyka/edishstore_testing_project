from random import randrange


class CommonTestData:
    def __init__(self):
        self.__sample_user_data_dict = dict(name="Smith",
                                            login="smith",
                                            email="smith1234@domain.com",
                                            number="0936739573",
                                            password="B12345")
        self.__nav_bar_text_data_dict = dict(name="Smith",
                                             login="smith",
                                             email="smith1234@domain.com",
                                             number="0936739573",
                                             password="B12345")
        self.__registration_empty_form_validation_messages_dict = dict(name="Укажите имя",
                                                                       login="Укажите логин",
                                                                       email="Укажите адрес почты",
                                                                       number="Укажите номер телефона",
                                                                       password="Укажите пароль")
        self.__registration_form_email_validation_messages_dict = dict(missed_username="Введите часть адреса до "
                                                                                       "символа \"@\". Адрес "
                                                                                       "\"@gmail.com\" неполный.",
                                                                       missed_domain="Недопустимое положение символа "
                                                                                     "\".\" в адресе \".com\".",
                                                                       missed_second_domain="Недопустимое положение "
                                                                                            "символа \".\" в адресе "
                                                                                            "\"domain.\".",
                                                                       missed_at_symbol="Адрес электронной почты "
                                                                                        "должен содержать символ "
                                                                                        "\"@\". В адресе "
                                                                                        "\"domain.com\" отсутствует "
                                                                                        "символ \"@\".")
        self.__nav_bar_button_text_dict = dict(login="Войти",
                                               registration="Регистрация")
        self.__information_messages_text_dict = dict(wrong_login_details="Неправильный логин или пароль")
        self.__rand_range = randrange(100000, 999999)

    def __get_sample_user_data_by_title(self, key: str) -> str:
        return self.__sample_user_data_dict.get(key)

    def __get_nav_bar_data_by_title(self, key: str) -> str:
        return self.__nav_bar_text_data_dict.get(key)

    def get_registration_empty_form_validation_messages_by_title(self, key: str) -> str:
        return self.__registration_empty_form_validation_messages_dict.get(key)

    def get_registration_form_email_validation_messages_by_title(self, key: str) -> str:
        return self.__registration_form_email_validation_messages_dict.get(key)

    def __get_nav_bar_button_text_by_title(self, key: str) -> str:
        return self.__nav_bar_button_text_dict.get(key)

    def get_name(self, rnd=True):
        name = self.__get_sample_user_data_by_title("name")
        if rnd:
            name += str(self.__rand_range)
        return name

    def get_login(self, rnd=True):
        login = self.__get_sample_user_data_by_title("login")
        if rnd:
            login += str(self.__rand_range)
        return login

    def get_email(self, rnd=True):
        email = self.__get_sample_user_data_by_title("login")
        if rnd:
            email = f"smith{str(self.__rand_range)}@gmail.com"
        return email

    def get_number(self, rnd=True):
        number = self.__get_sample_user_data_by_title("number")
        if rnd:
            number += f"093{str(self.__rand_range)}"
        return number

    def get_password(self, rnd=True):
        password = self.__get_sample_user_data_by_title('password')
        if rnd:
            password += str(self.__rand_range)
        return password

    def get_login_text(self):
        return self.__get_nav_bar_button_text_by_title("login")

    def get_information_message_text_by_title(self, key: str) -> str:
        return self.__information_messages_text_dict.get(key)
