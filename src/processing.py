import masks
import typing
import datetime


def filter_by_state(user_dicts: typing.Iterable[dict], state='EXECUTED') -> typing.Iterable[dict]:
    """ Функция для фильтрации словарей, в зависимости от переданного ключа"""
    new_dicts = []
    for one_dict in user_dicts:
        if one_dict['state'] == state:
            new_dicts.append(one_dict)

    return new_dicts


def sort_by_date(user_dicts: typing.Iterable[dict], reverse=False) -> typing.Iterable[dict]:
    """ Функция для сортировки словарей пользователя по дате"""

    return sorted(user_dicts, key=lambda item: datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=reverse)


a = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(sort_by_date(a))