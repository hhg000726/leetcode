class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while i * i < num:
            i += 1
        if i * i == num:
            return True
        else:
            return False