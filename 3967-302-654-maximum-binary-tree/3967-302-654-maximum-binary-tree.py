# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def func(l):
            if not l:
                return
            a = l.index(max(l))
            return TreeNode(max(l), func(l[:a]), func(l[a + 1:]))
        return func(nums)