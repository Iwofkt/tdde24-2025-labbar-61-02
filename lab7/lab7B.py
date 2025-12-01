
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


def tree_size(tree: list):
    size = 0

    def empty_tree_fn():
        return None

    def leaf_fn(key):
        nonlocal size
        if key:
            size += 1

    def inner_node_fn(key, left_value, right_value):
        nonlocal size
        size += 1

    # Treverse the tree to update the size value
    traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

    return size


def traverse(tree: list,
             inner_node_fn,
             leaf_fn,
             empty_tree_fn) -> int:

    def left_subtree(tree: list):
        return tree[0]

    def middle_subtree(tree: list):
        return tree[1]

    def right_subtree(tree: list):
        return tree[2]

    def subtree_calc(subtree):
        calced_tree = subtree(tree)
        if isinstance(calced_tree, list):
            value = leaf_fn(traverse(calced_tree,
                                     inner_node_fn,
                                     leaf_fn,
                                     empty_tree_fn))
        else:
            value = leaf_fn(calced_tree)

        return value

    if not tree:
        return empty_tree_fn()

    left_value = subtree_calc(left_subtree)
    right_value = subtree_calc(right_subtree)

    return inner_node_fn(
        middle_subtree(tree),
        left_value,
        right_value
    )


if __name__ == "__main__":
    print(traverse([[1,5,4], 7, [1,7,6]], left_inner_node_fn, leaf_fn, empty_tree_fn))
    print(contains_key([[1,5,4], 7, [1,8,[1,5,9]]], 10))
    print(tree_size([2, 7, []]))
    print(tree_size([]))
    print(tree_size([[1, 2, []], 4, [[], 5, 6]]))
