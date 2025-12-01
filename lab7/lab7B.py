
# Deluppgift 1
def empty_tree_fn():
    return 0


def leaf_fn(key):
    return key**2


def left_inner_node_fn(key, left_value, right_value):
    return key + left_value


def right_inner_node_fn(key, left_value, right_value):
    return key + right_value


# Deluppgift 2
def contains_key(tree, wanted_key):
    def empty_tree_fn():
        return 0

    def leaf_fn(key):
        if key == wanted_key:
            return True
        if isinstance(key, bool):
            return key
        return False

    def inner_node_fn(key, left_value, right_value):
        if key == wanted_key or left_value or right_value:
            return True
        return False

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_size(tree):
    def empty_tree_fn():
        return 0

    def leaf_fn(key):
        return 1

    def inner_node_fn(key, left_value, right_value):
        return 1 + left_value + right_value

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def traverse(tree,
                   inner_node_fn,
                   leaf_fn,
                   empty_tree_fn):
    if isinstance(tree, list):
        if not tree:  # Empty tree
            return empty_tree_fn()

        # Helper functions for accessing tree parts
        def left_subtree(t):
            return t[0]

        def key(t):
            return t[1]

        def right_subtree(t):
            return t[2]

        # Recursively process left and right subtrees
        left_value = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)
        right_value = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)

        return inner_node_fn(key(tree), left_value, right_value)
    else:
        # Leaf node
        return leaf_fn(tree)


if __name__ == "__main__":
    print(traverse([[1,5,4], 7, [1,7,6]], left_inner_node_fn, leaf_fn, empty_tree_fn))
    print(contains_key([[1,5,4], 7, [1,8,[1,5,9]]], 10))
    print(tree_size([2, 7, []]))
    print(tree_size([]))
    print(tree_size([[1, 2, []], 4, [[], 5, 6]]))
