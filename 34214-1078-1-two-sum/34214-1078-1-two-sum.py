class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - nums[i]) + i + 1]
    #Check if there is the number that target - each number in leftover list(from i + 1 to end). If it is, return i and that's index.
