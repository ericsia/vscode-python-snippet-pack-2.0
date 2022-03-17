from src.binary_tree import BinarySearchTree


class TestBinarySearchTree():
    @staticmethod
    def _get_binary_search_tree() -> BinarySearchTree:
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13
             \
              5
        """
        t = BinarySearchTree()
        t.put(8)
        t.put(3)
        t.put(6)
        t.put(1)
        t.put(10)
        t.put(14)
        t.put(13)
        t.put(4)
        t.put(7)
        t.put(5)

        return t

    def test_put(self) -> None:
        t = BinarySearchTree()
        assert t.is_empty()

        t.put(8)
        r"""
              8
        """
        assert t.root is not None
        assert t.root.parent is None
        assert t.root.label == 8

        t.put(10)
        r"""
              8
               \
                10
        """
        assert t.root.right is not None
        assert t.root.right.parent == t.root
        assert t.root.right.label == 10

        t.put(3)
        r"""
              8
             / \
            3   10
        """
        assert t.root.left is not None
        assert t.root.left.parent == t.root
        assert t.root.left.label == 3

        t.put(6)
        r"""
              8
             / \
            3   10
             \
              6
        """
        assert t.root.left.right is not None
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.right.label == 6

        t.put(1)
        r"""
              8
             / \
            3   10
           / \
          1   6
        """
        assert t.root.left.left is not None
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.left.label == 1

        with self.assertRaises(Exception):
            t.put(1)

    def test_search(self) -> None:
        t = self._get_binary_search_tree()

        node = t.search(6)
        assert node.label == 6

        node = t.search(13)
        assert node.label == 13

        with self.assertRaises(Exception):
            t.search(2)

    def test_remove(self) -> None:
        t = self._get_binary_search_tree()

        t.remove(13)
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \
            4   7
             \
              5
        """
        assert t.root is not None
        assert t.root.right is not None
        assert t.root.right.right is not None
        assert t.root.right.right.right is None
        assert t.root.right.right.left is None

        t.remove(7)
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             /
            4
             \
              5
        """
        assert t.root.left is not None
        assert t.root.left.right is not None
        assert t.root.left.right.left is not None
        assert t.root.left.right.right is None
        assert t.root.left.right.left.label == 4

        t.remove(6)
        r"""
              8
             / \
            3   10
           / \    \
          1   4    14
               \
                5
        """
        assert t.root.left.left is not None
        assert t.root.left.right.right is not None
        assert t.root.left.left.label == 1
        assert t.root.left.right.label == 4
        assert t.root.left.right.right.label == 5
        assert t.root.left.right.left is None
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.parent == t.root.left

        t.remove(3)
        r"""
              8
             / \
            4   10
           / \    \
          1   5    14
        """
        assert t.root is not None
        assert t.root.left.label == 4
        assert t.root.left.right.label == 5
        assert t.root.left.left.label == 1
        assert t.root.left.parent == t.root
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.parent == t.root.left

        t.remove(4)
        r"""
              8
             / \
            5   10
           /      \
          1        14
        """
        assert t.root.left is not None
        assert t.root.left.left is not None
        assert t.root.left.label == 5
        assert t.root.left.right is None
        assert t.root.left.left.label == 1
        assert t.root.left.parent == t.root
        assert t.root.left.left.parent == t.root.left

    def test_remove_2(self) -> None:
        t = self._get_binary_search_tree()

        t.remove(3)
        r"""
              8
             / \
            4   10
           / \    \
          1   6    14
             / \   /
            5   7 13
        """
        assert t.root is not None
        assert t.root.left is not None
        assert t.root.left.left is not None
        assert t.root.left.right is not None
        assert t.root.left.right.left is not None
        assert t.root.left.right.right is not None
        assert t.root.left.label == 4
        assert t.root.left.right.label == 6
        assert t.root.left.left.label == 1
        assert t.root.left.right.right.label == 7
        assert t.root.left.right.left.label == 5
        assert t.root.left.parent == t.root
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.left.parent == t.root.left.right

    def test_empty(self) -> None:
        t = self._get_binary_search_tree()
        t.empty()
        assert t.root is None

    def test_is_empty(self) -> None:
        t = self._get_binary_search_tree()
        assert not t.is_empty()

        t.empty()
        assert t.is_empty()

    def test_exists(self) -> None:
        t = self._get_binary_search_tree()

        assert t.exists(6)
        assert not t.exists(-1)

    def test_get_max_label(self) -> None:
        t = self._get_binary_search_tree()

        assert t.get_max_label() == 14

        t.empty()
        with self.assertRaises(Exception):
            t.get_max_label()

    def test_get_min_label(self) -> None:
        t = self._get_binary_search_tree()

        assert t.get_min_label() == 1

        t.empty()
        with self.assertRaises(Exception):
            t.get_min_label()

    def test_inorder_traversal(self) -> None:
        t = self._get_binary_search_tree()

        inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
        assert inorder_traversal_nodes == [1, 3, 4, 5, 6, 7, 8, 10, 13, 14]

    def test_preorder_traversal(self) -> None:
        t = self._get_binary_search_tree()

        preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
        assert preorder_traversal_nodes == [8, 3, 1, 6, 4, 5, 7, 10, 14, 13]
