
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

    def subtree_calc(subtree):
        if isinstance(subtree(tree), list):
            value = leaf_fn(traverse(subtree(tree),
                                     inner_node_fn,
                                     leaf_fn,
                                     empty_tree_fn))
        else:
            value = leaf_fn(subtree(tree))

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
