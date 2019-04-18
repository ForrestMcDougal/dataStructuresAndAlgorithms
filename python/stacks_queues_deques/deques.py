"""
A deque, also known as a double-ended queue, is an ordered
collection of items similar to the queue. It has two ends,
a front and a rear, and the items remain positioned in the 
collection. New items can be added at either the front or
the rear. Existing items can also be removed from either end.
"""


class Deque(object):
    """
    Deque() creates a new deque that is empty. It needs no
    parameters and returns an empty deque.

    addFront(item) adds a new item to the front of the deque.
    It needs an item and returns nothing.

    addRear(item) adds a new item to the rear of the deque.
    It needs an item and returns nothing.

    removeFront() removes the front item from the deque. It
    needs no parameters and returns the item. The deque is 
    modified.

    removeRear() removes the rear item from the deque. It needs
    no parameters and returns the item. The deque is modified.

    isEmpty() tests to see whether the deque is empty. It needs
    no parameters and returns a boolean value.

    size() returns the number of items in the deque. It needs no
    parameters and returns an integer.
    """

    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def addFront(self, item: object) -> None:
        self.items.append(item)

    def addRear(self, item: object) -> None:
        self.items.insert(0, item)

    def removeFront(self) -> object:
        return self.items.pop()

    def removeRear(self) -> object:
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)
