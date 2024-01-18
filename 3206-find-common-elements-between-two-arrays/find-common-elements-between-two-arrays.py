class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans= []
        count = 0
        for i in nums1:
            if i in set(nums2):
                count+=1
        ans.append(count)
        count = 0
        for i in nums2:
            if i in set(nums1):
                count+=1
        ans.append(count)
        return ans
        
        