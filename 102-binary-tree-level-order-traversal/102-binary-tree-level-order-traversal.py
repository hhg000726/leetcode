# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue1 = [root]
        queue2 = []
        answer = []
        newlevel = True
        while queue1 or queue2:
            while queue1:
                t = queue1.pop(0)
                if newlevel:
                    answer.append([t.val])
                    newlevel = False
                else:
                    answer[-1].append(t.val)
                if t.left:
                    queue2.append(t.left)
                if t.right:
                    queue2.append(t.right)
            newlevel = True
            while queue2:
                t = queue2.pop(0)
                if newlevel:
                    answer.append([t.val])
                    newlevel = False
                else:
                    answer[-1].append(t.val)
                if t.left:
                    queue1.append(t.left)
                if t.right:
                    queue1.append(t.right)
            newlevel = True
        return answer