class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        for i in nums2:
            if i in nums1:
                answer.add(i)
        return list(answer)