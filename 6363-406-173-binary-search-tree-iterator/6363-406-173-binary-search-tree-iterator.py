# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    i = 0
    l = []

    def __init__(self, root: Optional[TreeNode]):
        
        self.i = 0
        
        def func(a):
            if a.left:
                if a.right:
                    return func(a.left) + [a.val] + func(a.right)
                else:
                    return func(a.left) + [a.val]
            else:
                if a.right:
                    return [a.val] + func(a.right)
                else:
                    return [a.val]
        self.l = func(root)

    def next(self) -> int:
        ret = self.i
        self.i += 1
        return self.l[ret]

    def hasNext(self) -> bool:
        if self.i < len(self.l):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()