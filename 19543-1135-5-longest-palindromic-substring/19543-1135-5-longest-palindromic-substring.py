class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        answer = ""

        for i in range(len(s)):
            for j in range(len(s) - i):
                if s[j] == s[j + i]:
                    if i < 3 or dp[j + 1][j + i - 1] == True:
                        dp[j][j + i] = True
                        if i + 1 > len(answer):
                            answer = s[j:j + i + 1]
        return answer