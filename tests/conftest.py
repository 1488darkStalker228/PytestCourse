# Этот файл - coftest в глобальной области видимости;
import pytest
from random import randrange
from src.generators.player import Player


# Данная фикстура возвращает функцию;
@pytest.fixture
def calculate():
    return lambda a, b: a + b


@pytest.fixture
def make_number():
    print('ТО ЧТО ДО ТЕСТА')
    # Когда тест выполняется, сначала выполняется фикстура, а когда pytest видит елду то передаётся управление тесту.
    # Использование елды аналогично прокидыванию в тест функции;
    yield randrange(1, 1000, 5)


@pytest.fixture
def get_player_generator():
    return Player()
