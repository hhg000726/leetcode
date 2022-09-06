class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        notsn = set()
        an = set()
        sn = set()
        for i in edges:
            notsn.add(i[1])
            an.add(i[0])
        sn = an - notsn
        return list(sn)