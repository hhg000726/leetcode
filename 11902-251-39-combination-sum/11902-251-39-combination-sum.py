class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        answer = {}
        
        @cache
        def func(n, arr = ()):
            if n == 0:
                answer[arr] = True
                return
            if n > 0:
                for i in candidates:
                    t = list(arr) + [i]
                    t.sort()
                    func(n - i, tuple(t))
        
        func(target)
        return list(answer.keys())