class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        arr = []
        for i in nums2:
            if i in s1:
                arr.append(i)
        ans = list(set(arr))
        return ans