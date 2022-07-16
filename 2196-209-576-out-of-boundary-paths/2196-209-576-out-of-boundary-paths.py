class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:   
        @cache
        def func(i, j, x):
            if i == -1 or i == m or j == -1 or j == n:
                return 1
            if x == 0:
                return 0
            return func(i - 1, j, x - 1) + func(i + 1, j, x - 1) + func(i, j - 1, x - 1) + func(i, j + 1, x - 1) 
        
        return func(startRow, startColumn, maxMove) % 1000000007
                    