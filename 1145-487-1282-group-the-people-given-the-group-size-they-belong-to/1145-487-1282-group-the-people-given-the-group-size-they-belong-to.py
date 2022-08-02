class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        d = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]] = [i]
        for i in d:
            while len(d[i]) >= i:
                answer.append(d[i][0:i])
                d[i] = d[i][i:]
        return answer