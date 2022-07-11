import pytest
from src.baseclasses.response import Response
from src.schemas.user import User


# Название теста должно максимально описывать, что делает наш тест;
# В параметрах теста у нас используются фикстуры;
def test_getting_users_list(get_users, calculate, make_number):
    """
    Это пример комментария;
    С помощью данного теста валидируем получаемые данные;
    :param get_users: C помощью фикстуры получаем JSON;
    :param calculate: Фикстура, которая возвращает функцию;
    :param make_number: Фикстура в которой используется елда (Часть это фикстуры сработает до теста, а часть после);
    """
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate_pydantic(User)
    print(calculate(1, 2))
    print(make_number)


# Таким образом тесты можно скипать;
# @pytest.mark.skip('reason...')

# С помощью @pytest.mark.development добавляем тестам теги;
@pytest.mark.development
@pytest.mark.parametrize('a, b, result', [(1, 2, 3), (4, 5, 9)])
def test_calculation(a, b, result, calculate):
    assert calculate(a, b) == result
