import masks


def mask_account_card(bank_data: str) -> str:
    """ Функция для маскировки номеров счетов и карт"""
    bank_data_number = bank_data.split()[-1]  # Извлечение номера в формате str
    beginning = bank_data[:-len(bank_data_number)]  # Сохранение названия кроме номера

    if len(bank_data_number) == 16:  # Если номер карты, использовать модуль для карты
        mask_number = masks.get_mask_card_number(int(bank_data_number))
    else:  # Раз это не карта, использовать модуль для счёта
        mask_number = masks.get_mask_account(int(bank_data_number))

    return f"{beginning}{mask_number}"  # Возврат строки: Название + замаскированный номер


def get_date(date_string: str) -> str:
    """Функция для перевода даты из технического формата в читаемый"""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"  # Возврат извлечённых данных


# Данные для проверки
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Visa Classic 6831982476737658"))

# print(get_date("2024-03-11T02:26:18.671407"))
