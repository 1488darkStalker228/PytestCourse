from faker import Faker


class PlayerLocalization:
    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {'nickname': self.fake.first_name()}

    def set_number(self, number=11):
        self.result['number'] = number
        return self

    def set_test_value(self, value='value'):
        self.result['key'] = value
        return self

    def build(self):
        return self.result



