class Solution:
    answer = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.answer = []
        def func(node, r):
            if node == len(graph) - 1:
                self.answer.append(r)
            else:
                for i in graph[node]:
                    func(i, r + [i])
        func(0, [0])
        return self.answer