class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(n):
            if n <= 1:
                return 1
            else:
                return n * f(n - 1)
        return int(f(m + n - 2) / (f(n - 1) * f(m - 1)))