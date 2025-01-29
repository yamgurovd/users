from typing import Any
from requests import Response
from tests.src.helper.checker import negative_status_code, positive_status_code


def _assert_wrapper(value: Any,
                    error_message: str,
                    error_limit: int = 250) -> Any:
    if not value:
        raise AssertionError(error_message[:error_limit])


def status_code(response: Response,
                is_positive: bool = True) -> Any:
    """
    :param response: Проверяемый метод
    :param is_positive: Признак проверки позитивного/негативного набора статус кодов
    :return: Выполняется проверка статус кода в зависимости от контекста провекста проверки
    """

    if is_positive:
        return positive_status_code(response=response)
    else:
        return negative_status_code(response=response)


def equal(actual_result: Any,
          expected_result: Any,
          message: str,
          error_message: str | None = None) -> Any:
    """
    :param actual_result: Фактический результат
    :param expected_result: Ожидаемый результат
    :param message: Передоваемый текст
    :param error_message: Текст ошибки
    :return: Проверка
    """
    if error_message is None:
        error_message = (
            f"(equal){message}, actual_result: {actual_result}, expected_result: {expected_result}"
        )
        _assert_wrapper(actual_result == expected_result, error_message=error_message)
