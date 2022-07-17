class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if (s[i].isupper() and (s[i].lower() == s[i + 1])) or (s[i + 1].isupper() and (s[i + 1].lower() == s[i])):
                s = s[:i] + s[i + 2:]
                i -= 1
                i = max(i, 0)
            else:
                i += 1
        return s