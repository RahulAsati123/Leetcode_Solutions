class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # nums.sort(reverse=True)
        m = {}
        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if m[nums[i]] > m[nums[j]]:
                    nums[i],nums[j] = nums[j],nums[i]
                elif m[nums[i]] == m[nums[j]]:
                    if nums[i]<nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
        
        return nums
        