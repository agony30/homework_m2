import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("0000000000000000") == "0000 00** **** 0000"
    with pytest.raises(ValueError):
        get_mask_card_number("0")
    with pytest.raises(ValueError):
        get_mask_card_number("")
    with pytest.raises(ValueError):
        get_mask_card_number(None)


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("11111111111111111111") == "**1111"
    with pytest.raises(ValueError):
        get_mask_account("0")
    with pytest.raises(ValueError):
        get_mask_account("")
    with pytest.raises(ValueError):
        get_mask_account(None)
