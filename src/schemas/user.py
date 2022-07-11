from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors


# Данный класс является pydantic-моделью;
class User(BaseModel):
    # Таким образом, мы говорим пиздантику, что поле необязательное;
    # У пиздантика так же много других возможностей валидации, если что - гуглить;
    id: int = 0
    name: str
    email: str
    gender: Genders
    status: Statuses

    # Кастомный валидатор
    @validator('id')
    def check_id_len(cls, id):
        if id > 5:
            raise ValueError('id > 5, Слишком длинное id')
        else:
            return id

    @validator('email')
    def check_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)

