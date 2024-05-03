class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        box = set(nums)
        nums.sort()
        nums.reverse()
        for i in nums:
            if -i in box:
                return i
        return -1
    
        