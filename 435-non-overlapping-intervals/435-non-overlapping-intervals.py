#그리디 문제라는 사실에 집중했을때 해결방법을 찾을 수 있었다.
#각 구간이 들어올 때 마다 조건을 보고 어느쪽을 선택할지 고르면 되는 간단한 문제였다.
#여기서는 정렬 이후 직전의 구간과 비교해서 직전 end보다 이후 start가 높거나 같으면 넘어가고 아니라면 비교해서 더 end가 작은 쪽을 선택하면 된다.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        count = 0
        intervals.sort()
        while i < len(intervals) - 1:
            if intervals[i + 1][0] < intervals[i][1]:
                if intervals[i + 1][1] < intervals[i][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i + 1)
                count += 1
            else:
                i += 1
        return count
