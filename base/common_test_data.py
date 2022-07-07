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
        self.__registration_validation_messages_dict = dict(name="Укажите имя",
                                                            login="Укажите логин",
                                                            email="Укажите адрес почты",
                                                            number="Укажите номер телефона",
                                                            password="Укажите пароль")
        self.__rand_range = randrange(100000, 999999)

    def __get_sample_user_data_by_title(self, key: str) -> str:
        return self.__sample_user_data_dict.get(key)

    def __get_nav_bar_data_by_title(self, key: str) -> str:
        return self.__nav_bar_text_data_dict.get(key)

    def get_registration_validation_messages_by_title(self, key: str) -> str:
        return self.__registration_validation_messages_dict.get(key)

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
        return self.__get_nav_bar_data_by_title("login_text")
