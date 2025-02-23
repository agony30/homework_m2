def get_mask_card_number(card_number: str = "") -> str:
    """Функция для возврата маски номера карты"""

    if not card_number or len(card_number) != 16:  # Проверка на наличие номера
        raise ValueError("waiting 16")
    mask_card_number: str = ""

    for i, digit in enumerate(card_number):
        if i % 4 == 0 and i != 0:  # вставка пробелов через каждые 4 цифры
            mask_card_number += " "
        if 5 < i < len(card_number) - 4:
            mask_card_number += "*"
        else:
            mask_card_number += digit

    return mask_card_number


def get_mask_account(account: str = "") -> str:
    """Функция для возврата маски номера счёта (аккаунта)"""

    if not account or len(account) != 20:  # Проверка на наличие номера
        raise ValueError("waiting 20")

    return f"**{account[-4:]}"
