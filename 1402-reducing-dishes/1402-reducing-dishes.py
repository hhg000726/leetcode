class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        i = 0
        answer = 0
        s = 0
        t = []
        while i < len(satisfaction):
            if satisfaction[i] >= 0:
                s = sum(satisfaction[i:])
                t = satisfaction[i:]
                satisfaction = satisfaction[0:i:]
                satisfaction = satisfaction[::-1]
            i += 1
        for i in satisfaction:
            if s + i > 0:
                s += i
                t = [i] + t
        for i in range(len(t)):
            answer += (i + 1) * t[i]
        return answer