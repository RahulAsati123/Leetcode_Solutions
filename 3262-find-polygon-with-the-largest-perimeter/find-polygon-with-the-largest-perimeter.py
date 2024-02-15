class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        index = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<sum(nums[:i]):
                index +=i
                break
        if index == 0:
            return -1
        return sum(nums[:index+1])

        
        