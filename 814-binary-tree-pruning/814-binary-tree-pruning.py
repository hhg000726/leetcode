# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def func(node):
            if node.val == 0:
                l = True
                r = True
                if node.left:
                    l = func(node.left)
                if node.right:
                    r = func(node.right)
                if l and r:
                    node.left = None
                    node.right = None
                    return True
                elif l:
                    node.left = None
                    return False
                elif r:
                    node.right = None
                    return False
                else:
                    return False
            else:
                l = False
                r = False
                if node.left:
                    l = func(node.left)
                if node.right:
                    r = func(node.right)
                if l:
                    node.left = None
                if r:
                    node.right = None
                return False
        func(root)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root