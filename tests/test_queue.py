import pytest

# Use the project module, not Python's standard-library module named queue.
from src.queue import Queue


def test_queue_fifo():
    queue = Queue()
    assert len(queue) == 0
    assert not queue

    for value in [3, "hello", None]:
        queue.enqueue(value)

    assert len(queue) == 3
    assert bool(queue)
    assert queue.peek() == 3
    assert len(queue) == 3
    assert queue.dequeue() == 3

    queue.enqueue(7)
    assert queue.dequeue() == "hello"
    assert queue.dequeue() is None
    assert queue.dequeue() == 7
    assert len(queue) == 0
    assert not queue

    # An emptied queue must still accept new elements.
    queue.enqueue(9)
    assert queue.peek() == 9
    assert queue.dequeue() == 9
    assert not queue


def test_queue_empty_errors():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()

    queue.enqueue(1)
    queue.dequeue()
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()
