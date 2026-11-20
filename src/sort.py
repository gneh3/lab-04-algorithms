def insertion_sort(values: list[int]) -> list[int]:
    """Insertion sort. O(n^2). Returns sorted copy of original list."""
    check_sort(values)
    arr_copy: list[int] = values.copy()
    for i in range(1, len(arr_copy)):
        current: int = arr_copy[i]
        j: int = i - 1
        while j >= 0 and arr_copy[j] > current:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = current
    return arr_copy


def merge_sort(values: list[int]) -> list[int]:
    """Merge sort. O(n*log(n)). Returns sorted copy of original list."""
    check_sort(values)
    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return merge_sorted_lists(left, right)


def merge_sorted_lists(left: list[int], right: list[int]) -> list[int]:
    """Merge two presorted lists."""
    result: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def check_sort(values: list[int]) -> None:
    if type(values) is not list:
        raise TypeError("Value is not a list")
    for elem in values:
        if type(elem) is not int:
            raise TypeError("Value is not an integer")
