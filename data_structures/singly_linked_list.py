from typing import Any
from typing_extensions import Self


class Node:
    def __init__(self, value: Any = None) -> None:
        self._value = value
        self._next = None

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        self._value = value

    def __str__(self) -> str:
        return str(self.value)

class SinglyLinkedListIterator:
    def __init__(self, head: Node) -> None:
        self._current_node = head
        
    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Any:
        if not self._current_node:
            raise StopIteration
        else:
            node = self._current_node
            self._current_node = self._current_node.next
            return node

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __iter__(self) -> SinglyLinkedListIterator:
        return SinglyLinkedListIterator(self.head)

    def __str__(self) -> str:
        return '[' + ', '.join(str(node) for node in self) + ']'
        
    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, node: Node) -> None:
        self._head = node

    def insert(self, value: Any) -> None:
        '''
        Insert node to the linked list and swap head node
        '''
        node = Node(value)
        node.next = self.head
        self.head = node

    def reverse(self) -> Self:
        '''
        Reverse singly linked list inplace
        '''
        new_head = None  # set new head for linked list
        curr_node = self.head

        while curr_node:
            next_node = curr_node.next  # save next node
            curr_node.next = new_head  # link current node with new head
            new_head = curr_node  # set current node as new head
            curr_node = next_node  # set current node to the next one

        self.head = new_head
        return self


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    for i in range(1, 6):
        linked_list.insert(i)

    for node in linked_list:
        print(node)

    print(linked_list)
    print(linked_list.reverse())
