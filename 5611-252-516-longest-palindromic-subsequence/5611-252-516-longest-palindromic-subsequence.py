class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        answer = 0
        for i in range(len(s)):
            for j in range(len(s) - i):
                if s[j] == s[j + i]:
                    if i == 0:
                        dp[j][j] = 1
                    if i == 1:
                        dp[j][j + 1] = 2
                    if i > 1:
                        dp[j][j + i] = dp[j + 1][j + i - 1] + 2
                    answer = max(answer, dp[j][j + i])
                else:
                    dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
        return answer