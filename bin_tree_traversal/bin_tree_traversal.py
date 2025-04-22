"""bin_tree_traversal"""

class Node:
    """Node in binary tree"""
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    """RAB"""
    if node is None:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    """ARB"""
    if node is None:
        return []
    return  in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """ABR"""
    if node is None:
        return []
    return  post_order(node.left) + post_order(node.right) + [node.data]
