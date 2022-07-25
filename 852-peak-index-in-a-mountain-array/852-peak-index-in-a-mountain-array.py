class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def func(start, end):
            mid = (end + start) // 2
            if start > end:
                return
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return func(start, mid - 1)
            else:
                return func(mid + 1, end)
        return func(0, len(arr) - 1)