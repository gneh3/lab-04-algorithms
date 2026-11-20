from __future__ import annotations

# we'll do queue based on linked list to get O(1) deletion


class Node:
    def __init__(self, value: object, next_node: Node | None = None) -> None:
        self.value: object = value
        self.next: Node | None = next_node


class LinkedList:
    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def append(self, value: object) -> None:
        new_node: Node = Node(value)
        if self._size == 0:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def pop(self) -> object:
        if self._head is None:
            raise IndexError("Linked list is empty.")
        old_head: Node = self._head
        self._head = old_head.next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return old_head.value

    def __bool__(self) -> bool:
        return self._size > 0

    def peek(self) -> object:
        if self._head is None:
            raise IndexError("Linked list is empty.")
        return self._head.value
