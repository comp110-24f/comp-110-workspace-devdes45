"""EX04 - Utils - Calling function lists."""

__author__ = "730755654"

from utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return() -> None:
    input = [4, 3, 2, 1]
    assert only_evens(input) == [4, 2]


def test_only_evens_input() -> None:
    input = [4, 3, 2, 1]
    only_evens(input)
    assert input == [4, 3, 2, 1]


def test_only_evens_edge() -> None:
    input = [1, 3, 5]
    assert only_evens(input) == []


def test_sub_return() -> None:
    input = [4, 3, 2, 1]
    start = 1
    end = 3
    assert sub(input, start, end) == [3, 2, 1]


def test_sub_input() -> None:
    input = [4, 3, 2, 1]
    start = 1
    end = 3
    sub(input, start, end)
    assert input == [4, 3, 2, 1]


def test_sub_edge() -> None:
    input = [4, 3, 2, 1]
    start = -1
    end = 8
    assert sub(input, start, end) == [4, 3, 2, 1]


def test_add_at_index_return() -> None:
    input = [4, 3, 2, 1]
    num = 8
    idx = 2
    assert add_at_index(input, num, idx) is None


def test_add_at_index_input() -> None:
    input = [4, 3, 2, 1]
    num = 8
    idx = 2
    add_at_index(input, num, idx)
    assert input == [4, 3, 8, 2, 1]


def test_add_at_indexs_edge() -> None:
    input = [4, 3, 2, 1]
    num = 8
    idx = -1
    idx1 = 5
    with pytest.raises(IndexError):
        add_at_index(input, num, idx)
    with pytest.raises(IndexError):
        add_at_index(input, num, idx1)
