from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        # Здесь стоит добавить обработку ошибок;
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate_pydantic(self, schema):
        if isinstance(self.response_json, list):
            for i in self.response_json:
                schema.parse_obj(i)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        # status_code может быть листом для того, чтобы мы могли передать несколько ошибочных кодов состояния, и
        # система восприняла их как ошибочные;
        if isinstance(status_code, list):
            # Проверка на то, что число содержится в массиве. Self - это вызов волшебного метода __str__;
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self
    # Ожидаемый результат, который мы прописали = 200, если ФР == ОР, то всё заебись;
    # Мы можем прописать массив ожидаемых результатов, тогда происходит проверка, что
    # ФР-код, содержится в нашем массиве,
    # а если он не содержится, тогда будет вызвано сообщение GlobalErrorMessages.WRONG_STATUS_CODE.value;

    # Это волшебный метод, который помогает описать... а он нихуя нормально не объяснил;
    # В нём мы возвращаем подробную информацию о том, что мы получили в ошибочном респонсе;
    def __str__(self):
        return \
            f'\nStatus code: {self.response_status}; \n' \
            f'Requested url: {self.response.url}; \n' \
            f'Response body: {self.response_json}; \n' \
            f'Error message: {GlobalErrorMessages.WRONG_STATUS_CODE.value};'

