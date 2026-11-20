from linked_list import LinkedList


class Queue:
    """FI -- FO. Dequeue and peek raise IndexError when empty (from linked list)."""

    def __init__(self) -> None:
        self._items = LinkedList()

    def enqueue(self, item: object) -> None:
        self._items.append(item)

    def dequeue(self) -> object:
        return self._items.pop()

    def peek(self) -> object:
        return self._items.peek()

    def __len__(self) -> int:
        return len(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)
