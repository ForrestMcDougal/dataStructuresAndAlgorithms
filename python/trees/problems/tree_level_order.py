"""
GIven a binary tree of integers, print it in level order.
The output will contain space between the numbers in the same level,
and new line between different levels.
"""

import collections


class Node(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def level_order_print(tree):
    if not tree:
        return

    nodes = collections.deque([tree])

    current_count = 1
    next_count = 0

    while len(nodes) != 0:
        current_node = nodes.popleft()
        current_count -= 1
        print(current_node.value)

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1

        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1

        if current_count == 0:
            print('\n')
            current_count, next_count = next_count, current_count
