from fastapi import APIRouter, HTTPException
from back.user_schema import User, UserPATCH
from back.user_data import  fake_users

router = APIRouter(prefix="/users", tags=["Пользователи"])


class UserNotFoundException(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=404, detail=f"User with id {user_id} not found")


@router.get("", summary="Список пользователей")
def get_users():
    return fake_users


@router.get("/{user_id}", summary="Данные пользователя")
def get_user(user_id: int):
    user = next((user for user in fake_users if user["id"] == user_id), None)

    if user is None:
        raise UserNotFoundException(user_id)  # Используем исключение

    return user


@router.post("", summary="Создание пользователя")
def create_user(user_data: User):
    global fake_users

    new_id = fake_users[-1]["id"] + 1 if fake_users else 1
    fake_users.append({
        "id": new_id,
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "patronymic": user_data.patronymic,
        "phone_number": user_data.phone_number,
        "email": user_data.email,
        "company": user_data.company,
        "profession": user_data.profession,
    })

    return {"status": "Ok", "id": new_id}


@router.patch("/{user_id}", summary="Изменение данных пользователей")
def update_user(user_id: int, user_data: UserPATCH):
    global fake_users

    user = next((user for user in fake_users if user["id"] == user_id), None)

    if user is None:
        raise UserNotFoundException(user_id)  # Используем исключение

    # Обновляем поля при наличии данных
    if user_data.first_name is not None:
        user["first_name"] = user_data.first_name

    if user_data.last_name is not None:
        user["last_name"] = user_data.last_name

    if user_data.patronymic is not None:
        user["patronymic"] = user_data.patronymic

    if user_data.age is not None:
        user["age"] = user_data.age

    if user_data.phone_number is not None:
        user["phone_number"] = user_data.phone_number

    if user_data.email is not None:
        user["email"] = user_data.email

    if user_data.company is not None:
        user["company"] = user_data.company

    if user_data.profession is not None:
        user["profession"] = user_data.profession

    return {"status": "Ok"}


@router.delete("/{user_id}", summary="Удаление пользователя")
def delete_user(user_id: int):
    global fake_users

    user = next((user for user in fake_users if user["id"] == user_id), None)

    if user is None:
        raise UserNotFoundException(user_id)  # Используем исключение

    fake_users = [user for user in fake_users if user["id"] != user_id]

    return {"status": "Ok"}
