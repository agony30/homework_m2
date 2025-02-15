from pickle import GLOBAL

import pytest
from src.processing import filter_by_state, sort_by_date


# @pytest.mark.parametrize("user_dicts, state, filtered_dicts", [
#     ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
#      "EXECUTED",
#      [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
#
#     (([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
#      "CANCELED",
#      [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
# ])
# def test_filter_by_state(user_dicts, state, filtered_dicts):
#     assert filter_by_state(user_dicts, state) == filtered_dicts
#
# # Тестирование фильтрации списка словарей по заданному статусу state.
#
# # Проверка работы функции при отсутствии словарей с указанным
# # статусом state в списке.
#
# # Параметризация тестов для различных возможных значений статуса state.
# @pytest.mark.parametrize("user_dicts, reverse, sort_dicts", [
#     ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
#      True,
#      [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
#
#     ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
#      False,
#      [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#       {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
# ])
# def test_sort_by_date(user_dicts, reverse, sort_dicts):
#     assert sort_by_date(user_dicts, reverse) == sort_dicts

# Проверка корректности сортировки при одинаковых датах.
# Тесты на работу функции с некорректными или нестандартными форматами дат.

GLOBAL.filter_data_and_sorted = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# Код Ивана

@pytest.mark.parametrize("state, result", [
    ("EXECUTED", [
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}
    ]),
    ("CANCELED", [
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'}
    ]),
])
def test_filter_by_state(filter_data_and_sorted, state, result):
    assert filter_by_state(filter_data_and_sorted, state) == result
