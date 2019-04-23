"""Given a binary tree, check whether it's a binary search tree or not."""

tree_vals = []


def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        tree_vals.append(tree.get_root_val())
        inorder(tree.get_right_child())


def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)


# inorder(tree)
# sort_check(tree_vals)


class Node(object):
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


def tree_max(node):
    if not node:
        return float("-inf")
    max_left = tree_max(node.left)
    max_right = tree_max(node.right)
    return max(node.key, max_left, max_right)


def tree_min(node):
    if not node:
        return float("inf")
    min_left = tree_min(node.left)
    min_right = tree_min(node.right)
    return min(node.key, min_left, min_right)


def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and verify(node.left) and verify(node.right)):
        return True
    else:
        return False
