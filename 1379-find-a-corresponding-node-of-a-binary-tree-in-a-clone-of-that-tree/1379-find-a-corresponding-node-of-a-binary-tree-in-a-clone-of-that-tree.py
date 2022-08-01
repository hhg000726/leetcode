# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    answer = TreeNode()
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def func(node):
            if node.left:
                func(node.left)
            if node.right:
                func(node.right)
            if node.val == target.val:
                self.answer = node
        func(cloned)
        return self.answer