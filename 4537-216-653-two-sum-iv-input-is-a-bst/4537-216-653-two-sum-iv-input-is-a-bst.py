# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = set()
    answer = False
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.s = set()
        self.answer = False
        def func(node):
            if k - node.val in self.s:
                self.answer = True
            self.s.add(node.val)
            if node.left:
                func(node.left)
            if node.right:
                func(node.right)
        func(root)
        return self.answer