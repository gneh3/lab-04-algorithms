from random import Random

import pytest

from sort import insertion_sort, merge_sort, merge_sorted_lists


@pytest.mark.parametrize("function", [insertion_sort, merge_sort])
@pytest.mark.parametrize(
    "values",
    [
        [],
        [7],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 3, 1, 3],
        [-3, 0, -1, 2, -3],
    ],
)
def test_sort_values(function, values):
    original = values.copy()
    result = function(values)

    assert result == sorted(original)
    assert values == original
    assert result is not values


@pytest.mark.parametrize("function", [insertion_sort, merge_sort])
def test_sort_random_lists(function):
    rand = Random(42)
    for size in [2, 15, 100]:
        values = [rand.randint(-100, 100) for _ in range(size)]
        original = values.copy()
        assert function(values) == sorted(original)
        assert values == original


@pytest.mark.parametrize("function", [insertion_sort, merge_sort])
def test_sort_invalid_input(function):
    for value in [None, "123", (3, 1), [1, "2"], [1.5], [True]]:
        with pytest.raises(TypeError):
            function(value)


def test_merge_sorted_lists():
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([], [1, 2]) == [1, 2]
    assert merge_sorted_lists([1, 2], []) == [1, 2]
    left = [-3, 2, 2, 8]
    right = [-1, 2]
    assert merge_sorted_lists(left, right) == [-3, -1, 2, 2, 2, 8]
    assert left == [-3, 2, 2, 8]
    assert right == [-1, 2]
