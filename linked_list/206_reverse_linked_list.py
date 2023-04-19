from __future__ import annotations
from typing import Generic, TypeVar, Optional, TypeAlias


T = TypeVar('T')
LT = TypeVar('LT')


class ListNode(Generic[T]):
    def __init__(self, val: T | int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


# Solution1: iterative
def reverse_list_iteratively(head: Optional[ListNode[LT]]) -> Optional[ListNode[LT]]:
    current = head
    previous = None
    while current:
        buf = current.next
        current.next = previous
        previous = current
        current = buf
    head = previous
    return head


# Solution2: recursive
def reverse_list_recursively(head: Optional[ListNode[LT]]) -> Optional[ListNode[LT]]:
    ...


def create_list(data: list[LT]) -> Optional[ListNode[LT]]:
    head = ListNode(data[0])
    current = head
    for element in data[1:]:
        new_node = ListNode(element)
        current.next = new_node
        current = new_node

    return head


head = create_list(data=[1, 2, 3, 4, 5])
head = reverse_list_iteratively(head=head)
print(head.val)
