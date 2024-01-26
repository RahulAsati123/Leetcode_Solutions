class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                end = i
                break

        for i in range(start+1,len(nums)):
            if nums[i] == target:
                end = i
        return [start,end]
            
            
        