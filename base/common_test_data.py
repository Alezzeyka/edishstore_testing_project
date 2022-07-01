class CommonTestData:
    __test_data_dict = dict(name="Smith",
                            login="smith",
                            email="smith1234@domain.com",
                            number="0936739573",
                            password="B12345")

    def get_test_data_by_title(self, key: str) -> str:
        return self.__test_data_dict.get(key)
