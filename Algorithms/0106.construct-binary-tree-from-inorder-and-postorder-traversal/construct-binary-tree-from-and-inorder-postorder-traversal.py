from operator import index
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def tree(inorder_left:int, inorder_right:int, postorder_left:int, postorder_right:int) -> TreeNode:
            if postorder_left > postorder_right:
                return None

            postorder_root = postorder_right
            root_val = postorder[postorder_right]
            index_root = index[root_val]

            left_size =  index_root- inorder_left
            root = TreeNode(inorder[index_root])

            root.left = tree(inorder_left, index_root-1, postorder_left, postorder_left+left_size-1)
            root.right = tree(index_root+1, inorder_right, postorder_left+ left_size, postorder_right-1)
            return root
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return tree(0, len(inorder)-1, 0, len(postorder)-1)






