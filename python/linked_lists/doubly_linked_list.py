"""
A doubly linked list is a list in which each node keeps an explicit
reference to the node before it and a reference to the node after it.
These lists allow a greater variety of O(1)-time update operations,
including insertions and deletions. A "header" node is at the beginning of 
the list and a "trailer" node is at the end of the list. These "dummy"
nodes are known as sentinels (or guards). Every insertion into a doubly
linked list will take place between a pair of existing nodes. When a new
element is inserted at the front of the sequence, simply add the new
node between the header and the node that is currencly after the header.
To delete a node, the two neighbors of the node to be deleted are linked
directly to each other. As a result, the "deleted" node is simply no longer
attached to the list.
"""


class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b
