class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        box = {}
        n = len(nums)
        for i in nums:
            if i not in box:
                box[i] =1
            else:
                box[i]+=1
        for i in box:
            if box[i] > n//2:
                return i
            