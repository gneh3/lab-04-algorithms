from consts import RANDOM_SEED
from fibonacci import fibonacci_iterative, fibonacci_recursive
from generators import (
    duplicates_data,
    nearly_sorted_data,
    random_data,
    reversed_data,
    sorted_data,
)
from queue import Queue
from sort import insertion_sort, merge_sort


def main() -> None:
    n = 10
    print("Fibonacci, n =", n)
    print("Iterative:", fibonacci_iterative(n))
    print("Recursive:", fibonacci_recursive(n))

    values = [5, -2, 3, 5, 0, 1]
    print("Original list:", values)
    print("Insertion sort:", insertion_sort(values))
    print("Merge sort:", merge_sort(values))
    print("Original list after sorting:", values)

    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(7)
    queue.enqueue(2)
    print("Queue: added 3, 7, 2")
    print("Length:", len(queue))
    print("Not empty:", bool(queue))
    print("First element:", queue.peek())
    print("Length after peek:", len(queue))
    while queue:
        print("Dequeued:", queue.dequeue())
    print("Length:", len(queue))
    print("Not empty:", bool(queue))
    try:
        queue.dequeue()
    except IndexError as error:
        print("Empty queue error:", error)

    size = 10
    seed = RANDOM_SEED

    print("Random:", random_data(size, seed))
    print("Sorted:", sorted_data(size, seed))
    print("Reversed:", reversed_data(size, seed))
    print("Nearly sorted:", nearly_sorted_data(size, seed))
    print("Duplicates:", duplicates_data(size, seed))


if __name__ == "__main__":
    main()
