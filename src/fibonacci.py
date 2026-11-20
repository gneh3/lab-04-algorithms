def fibonacci_iterative(n: int) -> int:
    """Iterative fibonacci nums function"""
    validate_n(n)
    first: int = 0
    second: int = 1
    for _ in range(n):
        temp: int = first
        first = second
        second = temp + second
    return first


def fibonacci_recursive(n: int) -> int:
    """Recursive fibonacci nums function"""
    validate_n(n)  # runs every recursive call but could be extracted
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def validate_n(n: int) -> None:
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
