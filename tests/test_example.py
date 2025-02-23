# import pytest
# from src.example import add_func
#
#
# @pytest.mark.parametrize("bb, cc, dd", [(3, 5, 7), (1, 3, 5), (0, 2, 4)])
# def test_add_func1(aa, bb, cc, dd):
#     assert add_func(aa if aa else bb, bb) == cc
#     # assert add_func(aa, cc) == dd

# @pytest.mark.parametrize("aa, bb, cc", [(2, 5, 7), (1, 3, 14), (0, 2, 2)])
# def test_add_func1(aa, bb, cc):
#     assert add_func(aa, bb) == cc
#     assert add_func(aa, cc) == dd


# @pytest.mark.parametrize("bb, cc", [(33, 35), (20, 22), (0, 2)])
# def test_add_func2(example_a, bb, cc):
#     assert add_func(example_a, bb) == cc


# @pytest.mark.parametrize('username', ['directly-overridden-username'])
# def test_username(username):
#     assert username == 'directly-overridden-username'
#
# @pytest.mark.parametrize('username', ['directly-overridden-username-other'])
# def test_username_other(other_username):
#     assert other_username == 'other-directly-overridden-username-other'
