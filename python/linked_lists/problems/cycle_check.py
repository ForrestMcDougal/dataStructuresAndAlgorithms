"""
Given a singly linked list, write a function which takes in the first
node in a singly linked list and returns a boolean indicating if the 
linked list contains a "cycle". A cycle is when a node's next point
actually points back to a previou node in the list. This is also
sometimes known as a circularly linked list.

Solution:
use two markers to traverse the node list at different speeds. If 
the linked list is cyclical, the faster marker will "lap" the slower marker.
"""

import unittest


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check(node: Node) -> bool:
    """
    Checks to see if singly linked list is a cycle

    Arguments:
        node {Node} -- Node in singly linked list

    Returns:
        bool -- Whether or not the list is a cycle
    """

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


class TestCycleCheck(unittest.TestCase):
    def test_cycle_check(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        a.next_node = b
        b.next_node = c
        c.next_node = a
        x = Node(1)
        y = Node(2)
        z = Node(3)
        x.next_node = y
        y.next_node = z
        self.assertTrue(cycle_check(a))
        self.assertFalse(cycle_check(x))


if __name__ == '__main__':
    unittest.main()
