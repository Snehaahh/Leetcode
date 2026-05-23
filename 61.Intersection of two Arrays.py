class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2set = set(nums2)
        res = set()
        for num in nums1:
            if num in num2set:
                res.add(num)
        return list(res)
