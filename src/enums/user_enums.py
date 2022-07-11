from enum import Enum


# Не особо помню, как работают эти енамы;
class Genders(Enum):
    FEMALE = 'female'
    MALE = 'male'


class Statuses(Enum):
    INACTIVE = 'inactive'
    ACTIVE = 'active'


class UserErrors(Enum):
    WRONG_EMAIL = 'WRONG_EMAIL'
