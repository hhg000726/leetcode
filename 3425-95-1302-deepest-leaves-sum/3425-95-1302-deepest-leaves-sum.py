# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    level = 0
    answer = 0
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.level = 0
        self.answer= 0
        def func(node, l):
            if node.left:
                func(node.left, l + 1)
            if node.right:
                func(node.right, l + 1)
            if l == self.level:
                self.answer += node.val
            if l > self.level:
                self.level = l
                self.answer = node.val
        func(root, 0)
        return self.answer