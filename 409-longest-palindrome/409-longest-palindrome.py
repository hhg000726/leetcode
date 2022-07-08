class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        d = dict()
        answer = 0
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] % 2 == 0:
                answer += d[i]
            else:
                odd = True
                answer += d[i] - 1
        return answer + odd