"""
A stack is an ordered collection of items where the addition
of new items and the removal of existing items always takes
place at the same end, called the "top". The opposite end is
callsed the "base". last-in first-out (LIFO)
"""


class Stack(object):
    """
    Stack() creates a new stack that is empty. It needs no parameters
    and returns an empty stack

    push(item) adds a new item to the top of the stack. It need an item
    and returns nothing

    pop() removes the top item from the stack. It needs no parameters
    and returns the item. The stack is modified

    peek() returns the top item from the stack but does not remove it.
    It needs no parameters. The stack is not modified

    isEmpty() tests to see whether the stack is empty. It needs no 
    parameters and returns a boolean value

    size() returns the number of items on the stack. It needs no
    parameters and returns an integer
    """

    def __init__(self) -> list:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def push(self, item: object) -> None:
        self.items.append(item)

    def pop(self) -> object:
        return self.items.pop()

    def peek(self) -> object:
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)
