"""
Given the root of a binary search tree and 2 numbers min and max,
trin the tree such that all the numbers in the new tree are between
min and max (inclusive). The resulting tree should still be a valid
binary search tree.
"""


def trim_bst(tree, min_val, max_val):
    if not tree:
        return

    # post order traversal
    # process left children then right children than node itself.
    tree.left = trim_bst(tree.left, min_val, max_val)
    tree.right = trim_bst(tree.right, min_val, max_val)

    if min_val <= tree.val <= max_val:
        return tree

    if tree.val < min_val:
        return tree.right

    if tree.val > max_val:
        return tree.left
