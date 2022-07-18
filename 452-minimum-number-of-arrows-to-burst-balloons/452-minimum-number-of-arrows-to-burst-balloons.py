class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 1
        points.sort()
        end = points[0][1]
        for i in points[1:]:
            if i[0] > end:
                end = i[1]
                count += 1
            if i[1] < end:
                end = i[1]
        return count