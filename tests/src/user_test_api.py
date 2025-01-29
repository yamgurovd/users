from requests import Request

import json

from tests.src.helper.http_client import user_api_client
from tests.src.data.consts import GET_METHOD, DELETE_METHOD, PATCH_METHOD, POST_METHOD
from tests.src.helper.headers import headers


def get_id(id_: int):
    request = Request(
        method=GET_METHOD,
        url=f"users/{id_}"
    )
    response = user_api_client.send_request(request)

    return response


def delete(id_: int):
    request = Request(
        method=DELETE_METHOD,
        url=f"users/{id_}",
        headers=headers
    )
    response = user_api_client.send_request(request)

    return response


def post(first_name: str,
         last_name: str,
         patronymic: str,
         age: int,
         phone_number: str,
         email: str,
         company: str,
         profession: str):
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "age": age,
        "phone_number": phone_number,
        "email": email,
        "company": company,
        "profession": profession
    }
    request = Request(
        method=POST_METHOD,
        url="users",
        data=json.dumps(payload)
    )

    response = user_api_client.send_request(request)

    return response


def patch(id_: int,
          first_name: str | None = None,
          last_name: str | None = None,
          patronymic: str | None = None,
          age: int | None = None,
          phone_number: str | None = None,
          email: str | None = None,
          company: str | None = None,
          profession: str | None = None):
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "age": age,
        "phone_number": phone_number,
        "email": email,
        "company": company,
        "profession": profession
    }

    request = Request(
        method=PATCH_METHOD,
        url=f"users/{id_}",
        headers=headers,
        data=json.dumps(payload)
    )

    response = user_api_client.send_request(request)

    return response
