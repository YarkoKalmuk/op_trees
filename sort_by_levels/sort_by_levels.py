"""sort binary tree by levels"""
from collections import deque


class Node:
    """binary tree node"""
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.value = n

def tree_by_levels(node):
    """gives a sorted data of a tree"""
    result = []
    nodes_queue = deque()
    nodes_queue.append(node)
    while nodes_queue:
        popped = nodes_queue.popleft()
        if not popped:
            continue
        result.append(popped.value)
        nodes_queue.append(popped.left)
        nodes_queue.append(popped.right)
    return result

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))