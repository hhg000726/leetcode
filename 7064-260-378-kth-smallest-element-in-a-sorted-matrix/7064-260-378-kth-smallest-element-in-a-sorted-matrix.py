class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        t = []
        for i in matrix:
            t += i
        t.sort()
        return t[k - 1]