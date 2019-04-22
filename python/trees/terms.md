## Terms
* Node: the fundamental part of a tree. It can have a name, which is called the "key". A node may also have additional information. We call this additional information the "payload". While payload information is not central to many tree algorithms, it is often critical in applications that make use of trees.
* Edge: another fundamental part of the tree. An edge connects two nodes to show that there is a relationship between them. Every node (except the root) is connected by exactly one incoming edge from another node. Each node may have several outgoing edges.
* Root: The root fo the tree is the only node in the tree that has no incoming edges.
* Path: A path is an ordered list of nodes that are connected by edges.
* Children: The set of nodes "c" that have incoming edges from the same node are said to be children of that node.
* Parent: A node is the parent of all the nodes it connects to with outgoing edges.
* Siblings: Nodes in the tree that are children of the same parent are said to be siblings.
* Subtree: a set of nodes and edges comprised of a parent and all the descendants of that parent.
* Leaf: a node that has no children.
* Level: the level of a node "n" is the number of edges on the path from the root node to n.
* Height: the height of a tree is equal to the maximum level of any node in the tree.

## Full definition
* A tree consists of a set of nodes and a set of edges that connects pairs of nodes. A tree has the following properties:
    * One node of the tree is designated as the root node.
    * Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n.
    * A unique path traverses from the root to each node.
    * If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

## Recursive definition of a tree
* A tree is either empty of consists of a root and zero or one more subtrees, each of which is also a tree.
* The root of each subtree is connected to the root of the parent tree by an edge.