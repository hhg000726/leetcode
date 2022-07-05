class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        ans = [0] * len(ratings)
        d = dict()
        for i in range(len(ratings)):
            if ratings[i] in d:
                d[ratings[i]].append(i)
            else:
                d[ratings[i]] = [i]
        d = list(zip(d.keys(), d.values()))
        d.sort()
        for i in d:
            for j in i[1]:
                if j == 0:
                    ans[j] = ans[1] + 1
                elif j == len(ratings) - 1:
                    if ratings[-2] == ratings[-1]:
                        ans[j] = 1
                    else:
                        ans[j] = ans[-2] + 1
                else:
                    if ratings[j - 1] == ratings[j]:
                        ans[j] = ans[j + 1] + 1
                    else:    
                        ans[j] = max(ans[j - 1], ans[j + 1]) + 1
        return sum(ans)