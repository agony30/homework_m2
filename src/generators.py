from typing import Iterator


def filter_by_currency(transactions_list: list[dict], currency_code: str) -> Iterator[dict]:
    """Генератор словарей с транзакциями из переданного списка транзакций, по указанной валюте"""
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Iterator[str]:
    """Генератор описания транзакции из переданного списка транзакций"""
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start_num: int, finish_num: int) -> Iterator[str]:
    """Генератор номеров карт в указанном диапазоне"""
    while start_num <= finish_num:
        str_num = str(start_num).zfill(16)
        yield f"{str_num[0:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:16]}"
        start_num += 1


# код для проверки
# usd_transactions = filter_by_currency(a, "USD")
# for _ in range(2):
#     print(next(usd_transactions))

# for card_number in card_number_generator(2009, 2022):
#     print(card_number)
