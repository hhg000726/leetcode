# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []
        if not root:
            return self.answer
        def func(node, lst, s):
            if node.left:
                func(node.left, lst + [node.val], s + node.val)
            if node.right:
                func(node.right, lst + [node.val], s + node.val)
            if not node.left and not node.right and s + node.val == targetSum:
                self.answer.append(lst + [node.val])
        func(root, [], 0)
        return self.answer