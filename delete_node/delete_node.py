"""delete node"""

class TreeNode:
    """binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """solution"""
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        cur = root
        parent = None
        while cur.val != key:
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

            if cur is None:
                return root

        #two children
        if cur.left and cur.right:

            parent_of_smallest = cur
            smallest = cur.right
            while smallest.left:
                parent_of_smallest = smallest
                smallest = smallest.left

            cur.val = smallest.val

            if parent_of_smallest.left == smallest:
                parent_of_smallest.left = smallest.right
            else:
                parent_of_smallest.right = smallest.right

            return root


        #one child
        child = cur.left if cur.left else cur.right

        if parent is None:
            return child

        if parent.left == cur:
            parent.left = child
        else:
            parent.right = child

        return root


    def deleteNode_(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node with two children
            min_larger = self.get_min(root.right)
            root.val = min_larger.val
            root.right = self.deleteNode(root.right, min_larger.val)

        return root

    def get_min(self, node):
        while node.left:
            node = node.left
        return node


starting = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
result = Solution().deleteNode(starting, 3)
