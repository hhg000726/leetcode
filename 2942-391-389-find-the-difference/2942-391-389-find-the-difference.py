class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                return i
        for i in d:
            if d[i] != 0:
                return i