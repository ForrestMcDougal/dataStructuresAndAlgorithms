"""
Write a function to reverse a Linked List in place. The function
will take in the head of the list as input and return the new
head of the list.

Solution:
Space complexity is O(1) since it is in place
Time complexity is O(N)
In one pass from head to tail of our input list, point each node's
next pointer to the previous element. Make sure to copy current.next_node
into next_node before setting current.next_node to previous.
"""

import unittest


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head: Node) -> None:
    """
    Reverses a singly linked list in place

    Arguments:
        head {Node} -- Head node of singly linked list
    """

    current = head
    previous = None
    next_node = None

    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node

    return previous


class TestReverse(unittest.TestCase):
    def test_reverse(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.next_node = b
        b.next_node = c
        c.next_node = d
        reverse(a)
        self.assertEqual(d.next_node.value, 3)
        self.assertEqual(d.next_node, c)
        self.assertEqual(c.next_node.value, 2)
        self.assertEqual(c.next_node, b)
        self.assertEqual(b.next_node.value, 1)
        self.assertEqual(b.next_node, a)


if __name__ == '__main__':
    unittest.main()
