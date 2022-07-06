class Solution:
    def fib(self, n: int) -> int:
        dp1 = 0
        dp2 = 1
        for _ in range(n):
            dp1, dp2 = dp2, dp1 + dp2
        return dp1