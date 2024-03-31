class Solution:
   def fourSum(self,nums, target):
        nums.sort()
        res = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return list(res)
