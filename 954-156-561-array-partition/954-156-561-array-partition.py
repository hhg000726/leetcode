class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(int(len(nums) / 2)):
            answer += min(nums[2 * i], nums[2 * i + 1])
        return answer