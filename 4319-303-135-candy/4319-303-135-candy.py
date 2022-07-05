class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        blist, alist = [0] * len(ratings), [0] * len(ratings)
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
                    alist[j] = blist[1] + 1
                elif j == len(ratings) - 1:
                    alist[j] = blist[-2] + 1
                else:
                    alist[j] = max(blist[j - 1], blist[j + 1]) + 1
            blist = alist.copy()
        return sum(alist)
    #Make the list d, storing ratings and index in increasing order. Then add 1 from low ratings satisfying each conditions.
    #I had to consider the time for copying the data of alist to blist.
    #So I thought I must use only one list and add some 'if' statements in code.
