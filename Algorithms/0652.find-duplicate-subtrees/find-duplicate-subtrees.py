# Definition for a binary tree node.
import collections
import string
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = []
        self.dt = {}

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        self.tree(root)
        return self.res

    def tree(self, root):
        if root is None:
            return "#"
        # serial = "{},{},{}".format(root.val, self.tree(root.left), self.tree(root.right))
        serial = str(root.val) + "," + self.tree(root.left) + "," + self.tree(root.right)
        if serial not in self.dt:
            self.dt[serial] = 0
        if serial in self.dt:
            self.dt[serial] +=1
        if self.dt[serial] == 2:
            self.res.append(root)
        return serial

class Solution2:

    def __init__(self):
        self.res = []
        self.counter = collections.Counter()

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        self.tree(root)
        return self.res

    def tree(self, root):
        if root is None:
            return "#"
        # serial = "{},{},{}".format(root.val, self.tree(root.left), self.tree(root.right))
        serial = str(root.val) + "," + self.tree(root.left) + "," + self.tree(root.right)
        self.counter[serial] +=1
        if  self.counter[serial] == 2:
            self.res.append(root)
        return serial



class Solution:
    res = []
    memo = {}

    def __init__(self):
        self.res = []
        self.memo = {}

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root is None: return self.res
        self.traverse(root)
        return self.res

    def traverse(self, root):
        """序列化二叉树,采用后续遍历"""
        # 空节点，用 # 号代替
        if root is None: return "#"

        left = self.traverse(root.left)  # left为string类型
        right = self.traverse(root.right)  # right也为string类型

        # 描述整棵树
        subtree = left + "," + right + "," + str(root.val)  # subtree也为string类型
        if subtree in self.memo.keys() and self.memo[subtree] == 1:
            self.res.append(root)
            self.memo[subtree] += 1
        elif subtree not in self.memo.keys():
            self.memo[subtree] = 1

        return subtree
