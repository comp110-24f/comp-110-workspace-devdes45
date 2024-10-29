from find_max import find_and_remove_max


def test_find_test1() -> None:
    assert find_and_remove_max([1, 2, 5, 4, 5, 2, 5]) == 5


def test_remove_test2() -> None:
    test_list = [1, 2, 5, 4, 5, 2, 5]
    find_and_remove_max(test_list)
    assert test_list == [2, 4, 6, 8]


def test_negatives_test3() -> None:
    test_list: list[int] = [-1, -2, -4, 0, -8, 0]
    assert find_and_remove_max(test_list) == 0
