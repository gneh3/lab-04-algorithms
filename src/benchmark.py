import csv
from collections.abc import Callable
from time import perf_counter

from generators import (
    duplicates_data,
    nearly_sorted_data,
    random_data,
    reversed_data,
    sorted_data,
)
from sort import insertion_sort, merge_sort
from consts import (
    INPUT_SIZES,
    MILLISECONDS_PER_SECOND,
    RANDOM_SEED,
    REPEATS,
    RESULTS_FILE,
)


def measure_sort(
    sort_function: Callable[[list[int]], list[int]],
    values: list[int],
) -> list[float]:
    """Run a sort REPEATS times and return execution times in seconds."""
    times: list[float] = []
    expected = sorted(values)

    for _ in range(REPEATS):
        arr_copy = values.copy()

        start = perf_counter()
        result = sort_function(arr_copy)
        elapsed = perf_counter() - start

        if result != expected:
            raise AssertionError("Incorrect sorting result")
        if arr_copy != values:
            raise AssertionError("Sorting changed the original list")

        times.append(elapsed)

    return times


def run_benchmark() -> None:
    """Compare both sorts and save all measurements to CSV."""
    sorts = [insertion_sort, merge_sort]
    generators = {
        "random": random_data,
        "sorted": sorted_data,
        "reversed": reversed_data,
        "nearly_sorted": nearly_sorted_data,
        "duplicates": duplicates_data,
    }

    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["algorithm", "input_type", "size", "seed", "run", "seconds"])

        for size in INPUT_SIZES:
            for data_type, generator in generators.items():
                values = generator(size, RANDOM_SEED)

                for sort_function in sorts:
                    times = measure_sort(sort_function, values)

                    for i in range(len(times)):
                        writer.writerow(
                            [
                                sort_function.__name__,
                                data_type,
                                size,
                                RANDOM_SEED,
                                i + 1,
                                times[i],
                            ]
                        )

                    average = sum(times) / len(times)
                    print(
                        f"{sort_function.__name__}, {data_type}, size={size}: "
                        f"{average * MILLISECONDS_PER_SECOND:.3f} ms"
                    )

    print(f"Results saved to {RESULTS_FILE}")


if __name__ == "__main__":
    run_benchmark()
