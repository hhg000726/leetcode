class Solution:
    m = 100001
    M = -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.m = 100001
        self.M = -1
        def func(start, end):
            if start > end:
                return
            mid = (end + start) // 2
            if nums[mid] == target:
                self.m = min(self.m, mid)
                self.M = max(self.M, mid)
                func(start, mid - 1)
                func(mid + 1, end)
            elif target > nums[mid]:
                func(mid + 1, end)
            else:
                func(start, mid - 1)
        func(0, len(nums) - 1)
        if self.m == 100001:
            self.m = -1
        return [self.m, self.M]