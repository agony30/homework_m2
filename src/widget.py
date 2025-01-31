import masks


def mask_account_card(bank_data: str) -> str:
    """ Функция для маскировки номеров счетов и карт"""
    bank_data_number = bank_data.split()[-1]
    beginning = bank_data[:-len(bank_data_number)]

    if len(bank_data_number) == 16:
        mask_number = masks.get_mask_card_number(int(bank_data_number))
    else:
        mask_number = masks.get_mask_account(int(bank_data_number))

    return f"{beginning}{mask_number}"


# Данные для проверки
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
# print(mask_account_card("Счет 73654108430135874305"))
