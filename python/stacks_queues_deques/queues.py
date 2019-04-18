"""
A queue is an ordered collection of items where the addition
of new items happens at one end, called the "rear" and the 
removal of existing items occurs at the other end, commonly 
called the "front". As an element enters the queue it starts 
at the rear and makes its way toward the front, waiting until
that time when it is the next element to be removed. first-in
first-out (FIFO)

Enqueue is when you add a new item to the rear of a queue
Dequeue is when you remove an item from the front of the queue
"""


class Queue(object):
    """
    Queue() creates a new queue that is empty. It needs no parameters
    and returns an empty queue.

    enqueue(item) adds a new item to the rear of the queue. It needs
    an item and returns nothing.

    dequeue() removes the front item from the queue. It needs no
    parameters and returns the item. The queue is modified.

    isEmpty() tests to see whether the queue is empty. It needs no
    parameters and returns a boolean value.

    size() returns the number of items in the queue. It needs no parameters
    and returns an integer.
    """

    def __init__(self) -> list:
        self.items = []

    def isEmpty(self) -> bool:
        return self.items == []

    def enqueue(self, item: object) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> object:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)
