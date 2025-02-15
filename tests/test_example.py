import pytest

from src.example import reverse_list
from tests.conftest import example_list


# list_01 = example_list



@pytest.mark.parametrize("user_list", [example_list, [1, 5, 7], [1, 5, 7]])
def test_reverse_list_int1(user_list):
    assert reverse_list(user_list) == [7, 5, 1]
    # example_var.append(8)



# def test_reverse_list_int2(example_var):
#     print(example_var)
#     assert reverse_list(example_var) == [7, 5, 1]