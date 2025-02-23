from typing import Generator

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Проверьте, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
# Убедитесь, что генератор не завершается ошибкой при обработке пустого списка или
# списка без соответствующих валютных операций.
def test_filter_by_currency(transactions):
    assert isinstance(filter_by_currency(transactions, "USD"), Generator)

    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    rub_transactions = filter_by_currency(transactions, "RUB")
    assert next(rub_transactions) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


# Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.
# Попытаться использовать параметризацию
def test_transaction_descriptions(transactions):

    assert isinstance(transaction_descriptions(transactions), Generator)

    description_iter = transaction_descriptions(transactions)
    assert next(description_iter) == "Перевод организации"
    assert next(description_iter) == "Перевод со счета на счет"
    assert next(description_iter) == "Перевод со счета на счет"
    assert next(description_iter) == "Перевод с карты на карту"


# Проверьте корректность форматирования номеров карт.
# Убедитесь, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.
def test_card_number_generator():
    assert isinstance(card_number_generator(1, 5), Generator)
    numbers_gen = card_number_generator(1, 5)
    assert next(numbers_gen) == "0000 0000 0000 0001"
    assert next(numbers_gen) == "0000 0000 0000 0002"

    numbers_gen = card_number_generator(1009, 2000)
    assert next(numbers_gen) == "0000 0000 0000 1009"
    assert next(numbers_gen) == "0000 0000 0000 1010"
