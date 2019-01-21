"""
define a tree ----list version

"""

def tree(node, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [node] + list(branches)

def node(tree):
    """
    return the root of a tree
    """
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


"""
fib_tree
"""
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(node(left)+node(right), [left, right])

"""
count the number of leaves
"""
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(nextTree) for nextTree in branches(tree)])

"""
return list of leaves
"""
def leaves(tree):
    if is_leaf(tree):
        return [node(tree)]
    else:
        return sum([leaves(s) for s in branches(tree)], [])


"""
leaf +1
"""
def increment_leaves(t):
    if is_leaf(t):
        return tree(node(t) + 1)
    else :
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(node(t),bs)

"""
all nodes +1
"""
def increment(t):
    return tree(node(t) + 1, [increment(b) for b in branches(t)])











