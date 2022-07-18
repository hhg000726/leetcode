class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        l = []
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = [d[s[i]][0], i]
            else:
                d[s[i]] = [i, i]
        d = list(d.values())
        d.sort()
        l = [d[0]]
        for i in range(1, len(d)):
            new = True
            for j in range(len(l)):
                if d[i][0] <= l[j][1]:
                    if d[i][1] > l[j][1]:
                        l[j][1] = d[i][1]
                    new = False
                    break
            if new:
                l.append(d[i])
        for i in range(len(l)):
            l[i] = l[i][1] - l[i][0] + 1
        return l