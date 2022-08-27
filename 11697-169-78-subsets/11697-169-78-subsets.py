class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def func(sets, rem):
            t = []
            if rem:
                for i in sets:
                    t.append(i)
                    t.append(i + [rem[0]])
                return func(t, rem[1:])
            else:
                return sets
        return func([[], [nums[0]]], nums[1:])