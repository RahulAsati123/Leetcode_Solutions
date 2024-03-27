class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = left = 0
        prod = 1
        if k<=1:
            return 0
        for right,val in enumerate(nums):
            prod *=val
            while(prod>=k):
                prod /=nums[left]
                left+=1
            res+=(right-left+1)
        return res