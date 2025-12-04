
# Deluppgift 1
def empty_tree_fn():
    '''If the tree is empty returns 0'''
    return 0


def leaf_fn(key):
    '''If its a leaf return value of leaf raised to the second power'''
    return key**2


def left_inner_node_fn(key, left_value, right_value):
    '''Returns the left value + the middle value of a node'''
    return key + left_value


def right_inner_node_fn(key, left_value, right_value):
    '''Returns the right value + the middle value of a node'''
    return key + right_value


# Deluppgift 2
def contains_key(tree, wanted_key):
    '''Test if a binary tree contains a certain key'''
    
    def empty_tree_fn():
        '''If the tree is empty returns 0'''
        return 0

    def leaf_fn(key):
        '''Test if a leaf is either the wanted key or has returned True before
        if so return True else False'''
        if key == wanted_key:
            return True
        if isinstance(key, bool):
            return key
        return False

    def inner_node_fn(key, left_value, right_value):
        '''If the middle value of a node is the wanted key or the side values
        are True returns True else False'''
        if key == wanted_key or left_value or right_value:
            return True
        return False

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_size(tree):
    '''Gets the size of a binary tree'''

    def empty_tree_fn():
        '''If the tree is empty returns 0'''
        return 0

    def leaf_fn(key):
        '''If it's a leaf returns 1'''
        return 1

    def inner_node_fn(key, left_value, right_value):
        '''If it's a node returns 1 plus the size of the left and right side'''
        return 1 + left_value + right_value

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_depth(tree):
    '''Gets the depth of a binary tree'''

    def empty_tree_fn():
        '''If the tree is empty returns 0'''
        return 0

    def leaf_fn(key):
        '''If it's a lead returns 1'''
        return 1

    def inner_node_fn(key, left_value, right_value):
        '''If the tree is a node returns 1 plus the max of the size
        of left side and right side'''
        return 1 + max(left_value, right_value)

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def traverse(tree,
                   inner_node_fn,
                   leaf_fn,
                   empty_tree_fn):
    '''Recursively traverses a binary tree'''

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

    # If it's not a list it's a leaf
    else:
        # Leaf node
        return leaf_fn(tree)


if __name__ == "__main__":
    print(traverse([[1,5,4], 7, [1,7,6]], left_inner_node_fn, leaf_fn, empty_tree_fn))
    print(contains_key([[1,5,4], 7, [1,8,[1,5,9]]], 10))
    print(tree_size([2, 7, []]))
    print(tree_size([]))
    print(tree_size([[1, 2, []], 4, [[], 5, 6]]))
