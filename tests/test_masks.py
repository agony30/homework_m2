import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, mask_card_number", [
    (7000792289606361,"7000 79** **** 6361"),
    (1111111111111111,"1111 11** **** 1111"),
    (0,"0"),
    (None, "0")
])
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number

# Проверка работы функции на различных входных форматах номеров карт, включая
# граничные случаи и нестандартные длины номеров.


@pytest.mark.parametrize("account, mask_account", [
    (73654108430135874305,"**4305"),
    (11111111111111111111,"**1111"),
    (0,"0"),
    (None, "0")
])
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account


# Проверка работы функции с различными форматами и длинами номеров счетов.

# Проверка, что функция корректно обрабатывает входные данные,
# где номер счета меньше ожидаемой длины.
