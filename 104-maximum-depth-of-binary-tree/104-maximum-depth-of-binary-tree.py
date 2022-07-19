# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def func(node, depth):
            if depth > self.answer:
                self.answer = depth
            if node.left:
                func(node.left, depth + 1)
            if node.right:
                func(node.right, depth + 1)  
        func(root, 1)
        return self.answer