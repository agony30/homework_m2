import typing


def filter_by_state(user_dicts: typing.Iterable[dict], state='EXECUTED') -> typing.Iterable[dict]:
    """ Функция для фильтрации словарей, в зависимости от переданного ключа"""
    new_dicts = []  # Список словарей, которые будем возвращать
    for one_dict in user_dicts:  # Перебор поступивших словарей
        if one_dict['state'] == state:
            new_dicts.append(one_dict)

    return new_dicts


def sort_by_date(user_dicts: typing.Iterable[dict], reverse=False) -> typing.Iterable[dict]:
    """ Функция для сортировки словарей пользователя по дате"""

    return sorted(user_dicts, key=lambda x: x['date'], reverse=reverse)  # Сортировка по датам в формате str
