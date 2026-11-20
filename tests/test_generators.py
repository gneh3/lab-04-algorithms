import pytest

from generators import (
    duplicates_data,
    nearly_sorted_data,
    random_data,
    reversed_data,
    sorted_data,
)


@pytest.mark.parametrize(
    "generator",
    [
        random_data,
        sorted_data,
        reversed_data,
        nearly_sorted_data,
        duplicates_data,
    ],
)
def test_generator_size_and_seed(generator):
    for size in [0, 1, 2, 100]:
        values = generator(size, seed=42)
        assert isinstance(values, list)
        assert len(values) == size
        assert all(type(value) is int for value in values)
        assert values == generator(size, seed=42)

    assert generator(100, seed=42) != generator(100, seed=43)


@pytest.mark.parametrize(
    "generator",
    [
        random_data,
        sorted_data,
        reversed_data,
        nearly_sorted_data,
        duplicates_data,
    ],
)
def test_generator_invalid_size(generator):
    with pytest.raises(ValueError):
        generator(-1)

    for size in ["5", 2.5, None, True]:
        with pytest.raises(TypeError):
            generator(size)


def test_generated_order():
    values = random_data(100, seed=42)
    assert all(-100 <= value <= 100 for value in values)
    assert sorted_data(100, seed=42) == sorted(values)
    assert reversed_data(100, seed=42) == sorted(values, reverse=True)

    ordered = sorted_data(100, seed=42)
    nearly = nearly_sorted_data(100, seed=42)
    assert sorted(nearly) == ordered
    # Five swaps of neighbours can change at most ten positions.
    changed = sum(nearly[i] != ordered[i] for i in range(100))
    assert changed <= 10


def test_duplicates_range():
    values = duplicates_data(100, seed=42)
    assert all(-2 <= value <= 2 for value in values)
    assert len(set(values)) <= 5
    assert duplicates_data(4, seed=42, modulo_range=0) == [0, 0, 0, 0]
    assert all(
        -1 <= value <= 1 for value in duplicates_data(100, seed=42, modulo_range=1)
    )

    with pytest.raises(ValueError):
        duplicates_data(0, modulo_range=-1)
    for value in ["2", 1.5, None, True]:
        with pytest.raises(TypeError):
            duplicates_data(0, modulo_range=value)
