"""
In a list of lists tree, we will store the value of the root node as the 
first element of the list.
The second element of the list will itself be a list that represents the 
left subtree.
The third element of the list will be another list that represents the 
right subtree.
"""


def BinaryTree(r: object) -> list:
    """
    Create binary tree

    Arguments:
        r {object} -- root node

    Returns:
        list -- binary tree list object
    """
    return [r, [], []]


def insert_left(root: list, new_branch: object) -> list:
    """
    Insert Left child into tree

    Arguments:
        root {list} -- parent node
        new_branch {object} -- child node to be inserted

    Returns:
        list -- parent node with new child node
    """

    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root: list, new_branch: object) -> list:
    """
    Insert Right child into tree

    Arguments:
        root {list} -- parent node
        new_branch {object} -- child node to be inserted

    Returns:
        list -- parent node with new child node
    """

    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root: list) -> object:
    """
    Return root node value

    Arguments:
        root {list} -- tree

    Returns:
        object -- root value
    """

    return root[0]


def set_root_value(root: list, new_val: object):
    """
    Change root value

    Arguments:
        root {list} -- tree
        new_val {object} -- new root value
    """

    root[0] = new_val


def get_left_child(root: list) -> list:
    """
    Get left child

    Arguments:
        root {list} -- tree

    Returns:
        list -- left child
    """

    return root[1]


def get_right_child(root: list) -> list:
    """
    Get right child

    Arguments:
        root {list} -- tree

    Returns:
        list -- right child
    """

    return root[2]


r = BinaryTree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
