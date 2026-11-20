from random import Random


def random_data(size: int, seed: int | None = None) -> list[int]:
    validate_size(size)

    rand = Random(seed)
    return [rand.randint(-size, size) for _ in range(size)]


def sorted_data(size: int, seed: int | None = None) -> list[int]:
    random_lst = random_data(size, seed)
    return sorted(random_lst)


def reversed_data(size: int, seed: int | None = None) -> list[int]:
    random_lst = random_data(size, seed)
    return sorted(random_lst, reverse=True)


def nearly_sorted_data(size: int, seed: int | None = None) -> list[int]:
    sorted_lst = sorted_data(size, seed)
    if size < 2:
        return sorted_lst
    rand = Random(seed)
    for _ in range(max(1, size // 20)):
        switch_index: int = rand.randint(0, size - 2)
        sorted_lst[switch_index], sorted_lst[switch_index + 1] = (
            sorted_lst[switch_index + 1],
            sorted_lst[switch_index],
        )
    return sorted_lst


def duplicates_data(
    size: int, seed: int | None = None, *, modulo_range: int = 2
) -> list[int]:
    if type(modulo_range) is not int:
        raise TypeError("modulo_range must be an integer")
    if modulo_range < 0:
        raise ValueError("modulo_range must be non-negative")

    validate_size(size)
    rand = Random(seed)

    return [rand.randint(-modulo_range, modulo_range) for _ in range(size)]


def validate_size(size: int) -> None:
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be non-negative")
