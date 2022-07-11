from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


# Билдер - это класс, по умолчанию имеющий некие значения
class Player:
    """
    set методы создают в объекте result поля с определёнными полями, и возвращают self для того, чтобы мы могли
    изменять объект result вызовом цепочки методов;

    build метод - возвращает объект result;
    """
    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='https://www.google.com/'):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result['localize'] = {
            'en': PlayerLocalization('en_US').build(),
            'ru': PlayerLocalization('ru_RU').build()
        }
        return self

    def update_inner_generator(self, key, generator):
        self.result[key] = {'en': generator.build()}
        return self

    def build(self):
        return self.result



