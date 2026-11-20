import pytest

from fibonacci import fibonacci_iterative, fibonacci_recursive


@pytest.mark.parametrize("function", [fibonacci_iterative, fibonacci_recursive])
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (7, 13), (10, 55)])
def test_fibonacci_values(function, n, expected):
    assert function(n) == expected


@pytest.mark.parametrize("function", [fibonacci_iterative, fibonacci_recursive])
def test_fibonacci_invalid_input(function):
    with pytest.raises(ValueError):
        function(-1)

    for value in ["5", 2.5, None, True]:
        with pytest.raises(TypeError):
            function(value)
