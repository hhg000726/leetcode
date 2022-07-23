class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        answer= 0
        @cache
        def f(n):
            if n == 0:
                return 1
            else:
                return n * f(n - 1)
        @cache
        def c(n, r):
            return f(n) / (f(n - r) * f(r))
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] > 1:
                answer += c(d[i], 2)
        return int(answer)