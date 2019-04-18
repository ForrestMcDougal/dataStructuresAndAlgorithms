"""
Implement a Queue class using two stacks

Solution:
A stack reverses order (while a queue doesn't). A sequence of 
elements pushed on a stack comes back in reversed order when
popped. Consequently, two stacks chained together will return 
elements in the same order, since reversed order reversed again
is original order. Use an in-stack that you fill when an element
is enqueued and the dequeue operation takes elements from an out-stack.
If the out-stack is empty, pop all elements from the in-stack and push 
them onto the out-stack.
"""

import unittest


class Queue2Stacks(object):

    def __init__(self):
        # lists act as stacks here
        self.instack = []
        self.outstack = []

    def enqueue(self, element: object) -> None:
        self.instack.append(element)

    def dequeue(self) -> object:
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


class TestQueue2Stacks(unittest.TestCase):
    def test_Queue2Stacks(self):
        q = Queue2Stacks()
        for i in range(5):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)


if __name__ == '__main__':
    unittest.main()
