class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in range(len(strs)):
            t = str(sorted(list(strs[i])))
            if t not in d:
                d[t] = [strs[i]]
            else:
                d[t].append(strs[i])
        d = sorted(list(d.values()))
        return d
        