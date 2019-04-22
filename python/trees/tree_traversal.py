from python.trees.node_reference_implementation import BinaryTree


def preorder(tree: BinaryTree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value)


def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.getRootVal())
        inorder(tree.get_right_child())
