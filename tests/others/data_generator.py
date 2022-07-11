import pytest
from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_change_status(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'avatar',
    'balance',
    'localize'
])
def test_delete_key(delete_key, get_player_generator):
    """
    На каждой итерации удаляем одно из полей словаря;
    :param delete_key: поле, которое удаляем;
    :param get_player_generator: класс, возвращающий словарь;
    """
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_update_generator(get_player_generator):
    object_to_send = \
        get_player_generator.update_inner_generator(
            'localize', PlayerLocalization('fr_FR').set_number(15).set_test_value('dick')
        ).build()
    print(object_to_send)



