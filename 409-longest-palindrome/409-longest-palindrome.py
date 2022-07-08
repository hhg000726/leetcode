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
            answer += d[i]
            if d[i] % 2 != 0:
                odd = True
                answer -= 1
        return answer + odd