import math
import pytest

def calculate_logarithm(number):

    if number <= 0:
        raise ValueError("Логарифм можно вычислить только для положительных чисел")
    return math.log(number)


def test_calculate_logarithm_with_negative_number():
    with pytest.raises(ValueError) as exc_info:
        calculate_logarithm(-1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Логарифм можно вычислить только для положительных чисел"