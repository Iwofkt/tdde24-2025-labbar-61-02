
def empty_tree_fn():
    return 0


def leaf_fn(key):
    return key**2


def inner_node_fn(key, left_value, right_value):
    return key + left_value


def left_subtree(tree: list):
    return tree[0]


def right_subtree(tree: list):
    return tree[2]


def traverse(tree: list, 
             inner_node_fn: function, 
             leaf_fn: function, 
             empty_tree_fn: function) -> int:
    
    if not tree:
        return empty_tree_fn()
    
    if isinstance(left_subtree(tree), list):
        return traverse(left_subtree(tree))
    
    if 