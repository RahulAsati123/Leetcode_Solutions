class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >1:
            return [0]*len(nums)
        product = 1
        for i in nums:
            if i !=0:
                product *= i
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product 
                else:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
        return nums