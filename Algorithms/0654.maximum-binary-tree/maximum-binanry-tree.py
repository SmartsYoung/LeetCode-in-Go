from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        max = -1
        index = 0
        for i, v in enumerate(nums):
            if max < v:
                max = v
                index = i
        root = TreeNode(max)
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return root



if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,6,0,5]
    n = s.constructMaximumBinaryTree(nums)
    print(n)