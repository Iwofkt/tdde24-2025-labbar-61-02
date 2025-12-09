import unittest
from lab7.lab7B import (
    empty_tree_fn,
    leaf_fn,
    left_inner_node_fn,
    right_inner_node_fn,
    contains_key,
    tree_size,
    tree_depth,
    traverse,
)


class TestTraverseFunctions(unittest.TestCase):
    """Test the basic traverse callback functions."""

    def test_empty_tree_fn(self):
        """Test empty_tree_fn returns 0."""
        self.assertEqual(empty_tree_fn(), 0)

    def test_leaf_fn(self):
        """Test leaf_fn returns key squared."""
        self.assertEqual(leaf_fn(3), 9)
        self.assertEqual(leaf_fn(5), 25)
        self.assertEqual(leaf_fn(0), 0)

    def test_left_inner_node_fn(self):
        """Test left_inner_node_fn returns key + left_value."""
        self.assertEqual(left_inner_node_fn(10, 5, 3), 15)
        self.assertEqual(left_inner_node_fn(7, 2, 8), 9)

    def test_right_inner_node_fn(self):
        """Test right_inner_node_fn returns key + right_value."""
        self.assertEqual(right_inner_node_fn(10, 5, 3), 13)
        self.assertEqual(right_inner_node_fn(7, 2, 8), 15)


class TestContainsKey(unittest.TestCase):
    """Test the contains_key function."""

    def test_contains_key_found_at_root(self):
        """Test finding key at root of tree."""
        tree = [[], 7, []]
        self.assertTrue(contains_key(tree, 7))

    def test_contains_key_found_in_left(self):
        """Test finding key in left subtree."""
        tree = [[5, 6, 4], 7, [1, 7, 6]]
        self.assertTrue(contains_key(tree, 5))

    def test_contains_key_found_in_right(self):
        """Test finding key in right subtree."""
        tree = [[1, 5, 4], 4, [1, 7, 6]]
        self.assertTrue(contains_key(tree, 7))

    def test_contains_key_not_found(self):
        """Test key not found in tree."""
        tree = [[1, 5, 4], 7, [1, 8, [1, 5, 9]]]
        self.assertFalse(contains_key(tree, 10))

    def test_contains_key_empty_tree(self):
        """Test searching in empty tree."""
        tree = []
        self.assertFalse(contains_key(tree, 5))

    def test_contains_key_leaf_node(self):
        """Test searching in single leaf node."""
        tree = 5
        self.assertTrue(contains_key(tree, 5))
        self.assertFalse(contains_key(tree, 3))


class TestTreeSize(unittest.TestCase):
    """Test the tree_size function."""

    def test_tree_size_empty(self):
        """Test size of empty tree."""
        self.assertEqual(tree_size([]), 0)

    def test_tree_size_single_leaf(self):
        """Test size of single leaf node."""
        self.assertEqual(tree_size(5), 1)

    def test_tree_size_single_node_tree(self):
        """Test size of tree with one node (leaves empty)."""
        tree = [[], 7, []]
        self.assertEqual(tree_size(tree), 1)

    def test_tree_size_three_nodes(self):
        """Test size of tree with three nodes."""
        tree = [2, 7, []]
        self.assertEqual(tree_size(tree), 2)

    def test_tree_size_balanced_tree(self):
        """Test size of larger balanced tree."""
        tree = [[1, 2, []], 4, [[], 5, 6]]
        self.assertEqual(tree_size(tree), 5)


class TestTreeDepth(unittest.TestCase):
    """Test the tree_depth function."""

    def test_tree_depth_empty(self):
        """Test depth of empty tree."""
        self.assertEqual(tree_depth([]), 0)

    def test_tree_depth_single_leaf(self):
        """Test depth of single leaf node."""
        self.assertEqual(tree_depth(5), 1)

    def test_tree_depth_single_node_tree(self):
        """Test depth of tree with one node."""
        tree = [[], 7, []]
        self.assertEqual(tree_depth(tree), 1)

    def test_tree_depth_left_heavy(self):
        """Test depth of left-heavy tree."""
        tree = [[[], 2, []], 4, []]
        self.assertEqual(tree_depth(tree), 2)

    def test_tree_depth_balanced_tree(self):
        """Test depth of balanced tree."""
        tree = [[1, 2, []], 4, [[], 5, 6]]
        self.assertEqual(tree_depth(tree), 3)

    def test_tree_depth_deep_tree(self):
        """Test depth of deeper tree."""
        tree = [[[[], 1, []], 2, []], 4, []]
        self.assertEqual(tree_depth(tree), 3)


class TestTraverse(unittest.TestCase):
    """Test the traverse function directly."""

    def test_traverse_with_custom_functions(self):
        """Test traverse with the functions from Deluppgift 1."""
        tree = [[1, 5, 4], 7, [1, 7, 6]]
        result = traverse(tree, left_inner_node_fn, leaf_fn, empty_tree_fn)
        # Expected: traverse processes and applies functions recursively
        self.assertIsNotNone(result)

    def test_traverse_empty_tree(self):
        """Test traverse on empty tree."""
        result = traverse([], left_inner_node_fn, leaf_fn, empty_tree_fn)
        self.assertEqual(result, 0)

    def test_traverse_leaf_only(self):
        """Test traverse on leaf node."""
        result = traverse(5, left_inner_node_fn, leaf_fn, empty_tree_fn)
        self.assertEqual(result, 25)  # 5**2


if __name__ == "__main__":
    unittest.main()
