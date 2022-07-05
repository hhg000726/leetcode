class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        t = ""
        l = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in t:
                t = s[d[s[i]] + 1:i + 1]
                l = len(t)
            else:
                t += s[i]
                l += 1
            ans = max(ans, l)
            d[s[i]] = i
        return ans
    #Rememeber the last index of alphabet(using dictionary) in s to check from where I have to count characters and revise values.
