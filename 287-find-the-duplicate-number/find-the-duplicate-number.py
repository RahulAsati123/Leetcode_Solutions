class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # map = {}
        # for i in nums:
        #     if i not in map:
        #         map[i] = 1
        #     else:
        #         map[i]+=1
        # for i in map:
        #     if map[i] >1:
        #         return i
        nums.sort()
        for i in range(len(nums)):
            if nums[i]^nums[i+1] == 0:
                return nums[i]
        

