#DP로 접근했다. 같은 문자가 둘 있다면 그 사이의 문자열의 답에 2를 더한 것이 그 두 문자열을 포함한 문자열의 답이 될 것이다.
#같은 문자가 아니라면 앞 혹은 뒤의 문자를 포함하는 문자열 중 더 높은 값을 답으로 가져가면 된다.
#짧은 문자열부터 이를 반복하면 된다. 길이가 3보다 작은 경우는 if로 예외적으로 처리해준다.
#같은 문자열을 발견할때마다 answer값을 갱신해준다.

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
