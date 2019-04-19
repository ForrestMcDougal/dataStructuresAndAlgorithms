"""
Write a function that takes a head node and an integer value n 
and then returns the nth to last node in the linked list.

Solution:
using two pointers, move down the list with the first pointer n
spaces ahead. Once the first pointer hits the end, the second 
pointer is at the wanted node.
"""

import unittest


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def nth_to_last_node(n: int, head: Node) -> Node:
    """
    Returns nth to last node from singly linked list

    Arguments:
        n {int} -- position in linked list
        head {Node} -- head node of linked list

    Returns:
        Node -- nth to last node of linked list
    """

    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.next_node:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        right_pointer = right_pointer.next_node
        left_pointer = left_pointer.next_node

    return left_pointer


class TestNthToLastNode(unittest.TestCase):
    def test_nth_to_last_node(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        a.next_node = b
        b.next_node = c
        c.next_node = d
        d.next_node = e
        target_node = nth_to_last_node(2, a)
        self.assertEqual(target_node, d)
        self.assertEqual(target_node.value, 4)


if __name__ == '__main__':
    unittest.main()
