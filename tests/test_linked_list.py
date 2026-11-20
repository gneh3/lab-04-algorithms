import pytest

from linked_list import LinkedList


def test_linked_list_links_and_size():
    items = LinkedList()
    assert items._head is None
    assert items._tail is None
    assert len(items) == 0
    assert not items

    items.append(3)
    assert items._head is items._tail
    assert items._tail.next is None
    assert len(items) == 1

    items.append(7)
    assert items._head.next is items._tail
    assert items._tail.value == 7
    assert items._tail.next is None
    assert len(items) == 2
    assert bool(items)
    assert items.peek() == 3
    assert len(items) == 2

    assert items.pop() == 3
    assert items._head is items._tail
    assert len(items) == 1
    assert items.pop() == 7
    assert items._head is None
    assert items._tail is None
    assert len(items) == 0
    assert not items

    items.append(9)
    assert items.peek() == 9
    assert items._head is items._tail
    assert items._tail.next is None
    assert items.pop() == 9


def test_linked_list_empty_errors():
    items = LinkedList()
    with pytest.raises(IndexError):
        items.pop()
    with pytest.raises(IndexError):
        items.peek()
