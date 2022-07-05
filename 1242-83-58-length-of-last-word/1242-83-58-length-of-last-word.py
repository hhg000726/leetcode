class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])
    #split() function split the string by some standards(default is 'space bar')
