# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def func(node):
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            if node.val == 2:
                return func(node.left) or func(node.right)
            if node.val == 3:
                return func(node.left) and func(node.right)
        return func(root)