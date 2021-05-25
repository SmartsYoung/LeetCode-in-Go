import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def __init__(self):
        self.min_left = -math.inf


    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if key == root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            node = self.min_left_node(root.right, self.min_left)
            root.val =node.val
            root.right = self.deleteNode(root.right, node.val)

            return root
        elif key > root.val and root.right is not None:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        return root
    def min_left_node(self, node, min_left):
        while node.left is not None:
            node = node.left
        return node