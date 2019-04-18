"""
A singly linked list is a collection of nodes that collectively
form a linear sequence. Each node stores a reference to an object
that is an element of the next sequence, as well as a reference to
the next node of the list. The first and last node of a linked list
are known as the "head" and "tail" of the list. The "tail" has None
as its next reference. Each node is represented as a unique object,
with that instance storing a reference to its element and a reference
to the next node (or None). A linked list does not have a predetermined
fixed size. It uses space proportionally to its current number of elements.
To insert a new element at the head of the list:
* Create a new node
* Set its element to the new element
* Set its next link to refer to the current head
* Set the list's head to point to the new node
To insert a new element at the tail of the list:
* Create a new node
* Assign its next reference to None
* Set the reference of the tail to point to this new node
* Update the tail reference to this new node
You can remove a head from a singly linked list easily, but removing
the tail necessitates a doubly linked list.

Pros:
* Constant time insertion and deletion, where arrays require O(n)
time to do the same thing
* Continue to expand without specifying sizes beforehand
Cons:
* Access takes O(k) time to get to kth element, where arrays have
constant time operations to access any element in the array
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# create nodes
# a = Node(1)
# b = Node(2)
# c = Node(3)

# link the nodes
# a.nextnode = b
# b.nextnode = c

# get value of next node
# a.nextnode.value
