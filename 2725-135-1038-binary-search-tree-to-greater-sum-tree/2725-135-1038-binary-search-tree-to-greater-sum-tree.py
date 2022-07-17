# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def func(node):
            if node.right:
                func(node.right)
            self.s += node.val
            node.val = self.s
            if node.left:
                func(node.left)
        func(root)
        return root