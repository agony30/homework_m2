def get_mask_card_number(card_number: int) -> str:
    """Функция для возврата маски номера карты"""
    mask_card_number: str = ""
    for i, digit in enumerate(str(card_number)):
        if i % 4 == 0 and i != 0:  # вставка пробелов через каждые 4 цифры
            mask_card_number += " "
        if 5 < i < len(str(card_number)) - 4:
            mask_card_number += "*"
        else:
            mask_card_number += digit
    return mask_card_number


def get_mask_account(account: int) -> str:
    """Функция для возврата маски номера счёта (аккаунта)"""
    return "**" + str(account)[-4:]


# код проверки
# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
