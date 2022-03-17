from __future__ import annotations
from typing import Iterator


class Node:
    def __init__(self, label: int, parent: Node | None) -> None:
        self.label = label
        self.parent = parent
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    """
    This is a python3 implementation of binary search tree using recursion
    """
    def __init__(self) -> None:
        self.root: Node | None = None

    def empty(self) -> None:
        """
        Empties the tree

        >>> t = BinarySearchTree()
        >>> assert t.root is None
        >>> t.put(8)
        >>> assert t.root is not None
        """
        self.root = None

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty

        >>> t = BinarySearchTree()
        >>> t.is_empty()
        True
        >>> t.put(8)
        >>> t.is_empty()
        False
        """
        return self.root is None

    def put(self, label: int) -> None:
        """
        Put a new node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> assert t.root.parent is None
        >>> assert t.root.label == 8

        >>> t.put(10)
        >>> assert t.root.right.parent == t.root
        >>> assert t.root.right.label == 10

        >>> t.put(3)
        >>> assert t.root.left.parent == t.root
        >>> assert t.root.left.label == 3
        """
        self.root = self._put(self.root, label)

    def _put(self, node: Node | None, label: int, parent: Node | None = None) -> Node:
        if node is None:
            node = Node(label, parent)
        else:
            if label < node.label:
                node.left = self._put(node.left, label, node)
            elif label > node.label:
                node.right = self._put(node.right, label, node)
            else:
                raise Exception(f"Node with label {label} already exists")

        return node

    def search(self, label: int) -> Node:
        """
        Searches a node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> node = t.search(8)
        >>> assert node.label == 8

        >>> node = t.search(3)
        Traceback (most recent call last):
            ...
        Exception: Node with label 3 does not exist
        """
        return self._search(self.root, label)

    def _search(self, node: Node | None, label: int) -> Node:
        if node is None:
            raise Exception(f"Node with label {label} does not exist")
        else:
            if label < node.label:
                node = self._search(node.left, label)
            elif label > node.label:
                node = self._search(node.right, label)

        return node

    def remove(self, label: int) -> None:
        """
        Removes a node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.remove(8)
        >>> assert t.root.label == 10

        >>> t.remove(3)
        Traceback (most recent call last):
            ...
        Exception: Node with label 3 does not exist
        """
        node = self.search(label)
        if node.right and node.left:
            lowest_node = self._get_lowest_node(node.right)
            lowest_node.left = node.left
            lowest_node.right = node.right
            node.left.parent = lowest_node
            if node.right:
                node.right.parent = lowest_node
            self._reassign_nodes(node, lowest_node)
        elif not node.right and node.left:
            self._reassign_nodes(node, node.left)
        elif node.right and not node.left:
            self._reassign_nodes(node, node.right)
        else:
            self._reassign_nodes(node, None)

    def _reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        if new_children:
            new_children.parent = node.parent

        if node.parent:
            if node.parent.right == node:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def _get_lowest_node(self, node: Node) -> Node:
        if node.left:
            lowest_node = self._get_lowest_node(node.left)
        else:
            lowest_node = node
            self._reassign_nodes(node, node.right)

        return lowest_node

    def exists(self, label: int) -> bool:
        """
        Checks if a node exists in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.exists(8)
        True

        >>> t.exists(3)
        False
        """
        try:
            self.search(label)
            return True
        except Exception:
            return False

    def get_max_label(self) -> int:
        """
        Gets the max label inserted in the tree

        >>> t = BinarySearchTree()
        >>> t.get_max_label()
        Traceback (most recent call last):
            ...
        Exception: Binary search tree is empty

        >>> t.put(8)
        >>> t.put(10)
        >>> t.get_max_label()
        10
        """
        if self.root is None:
            raise Exception("Binary search tree is empty")

        node = self.root
        while node.right is not None:
            node = node.right

        return node.label

    def get_min_label(self) -> int:
        """
        Gets the min label inserted in the tree

        >>> t = BinarySearchTree()
        >>> t.get_min_label()
        Traceback (most recent call last):
            ...
        Exception: Binary search tree is empty

        >>> t.put(8)
        >>> t.put(10)
        >>> t.get_min_label()
        8
        """
        if self.root is None:
            raise Exception("Binary search tree is empty")

        node = self.root
        while node.left is not None:
            node = node.left

        return node.label

    def inorder_traversal(self) -> Iterator[Node]:
        """
        Return the inorder traversal of the tree

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.inorder_traversal()]
        []

        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for i in t.inorder_traversal()]
        [8, 9, 10]
        """
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node
            yield from self._inorder_traversal(node.right)

    def preorder_traversal(self) -> Iterator[Node]:
        """
        Return the preorder traversal of the tree

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.preorder_traversal()]
        []

        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for i in t.preorder_traversal()]
        [8, 10, 9]
        """
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield node
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)