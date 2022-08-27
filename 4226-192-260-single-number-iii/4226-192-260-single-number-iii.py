class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = []
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.append(i)
        return d