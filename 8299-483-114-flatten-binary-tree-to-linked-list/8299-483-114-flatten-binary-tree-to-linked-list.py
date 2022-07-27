# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def func(node):
            if not node:
                return
            if node.left:
                func(node.left)
                if node.right:
                    func(node.right)
                    bleft = node.left
                    bright = node.right
                    node.left = None
                    node.right = bleft
                    while bleft.right:
                        bleft = bleft.right
                    bleft.right = bright
                else:
                    node.right = node.left
                    node.left = None
            elif node.right:
                func(node.right)
        func(root)