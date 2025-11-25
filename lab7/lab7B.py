
def empty_tree_fn():
    return 0


def leaf_fn(key):
    return key**2


def left_inner_node_fn(key, left_value, right_value):
    return key + left_value


def right_inner_node_fn(key, left_value, right_value):
    return key + right_value


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

    if not tree:
        return empty_tree_fn()

    if isinstance(left_subtree(tree), list):
        return traverse(left_subtree(tree),
                        inner_node_fn, leaf_fn,
                        empty_tree_fn)

    return inner_node_fn(
        middle_subtree(tree),
        leaf_fn(left_subtree(tree)),
        leaf_fn(right_subtree(tree))
    )


if __name__ == "__main__":
    print(traverse([[1, 2, 1], 7, 8], left_inner_node_fn, leaf_fn, empty_tree_fn))
