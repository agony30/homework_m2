from typing import List


def filter_by_state(user_dicts: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """ Функция для фильтрации словарей, в зависимости от переданного ключа"""
    filtered_dicts: list = []  # Список словарей, которые будем возвращать
    for user_dict in user_dicts:  # Перебор поступивших словарей
        if user_dict['state'] == state:
            filtered_dicts.append(user_dict)

    return filtered_dicts


def sort_by_date(user_dicts: List[dict], reverse: bool = False) -> List[dict]:
    """ Функция для сортировки словарей пользователя по дате"""

    return sorted(user_dicts, key=lambda x: x['date'], reverse=reverse)  # Сортировка по датам в формате str
