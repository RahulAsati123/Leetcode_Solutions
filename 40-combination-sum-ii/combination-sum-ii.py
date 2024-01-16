class Solution:
    def ss(self,idx,arr,nums,target):
        if target == 0:
            self.ans.append(arr.copy())
            return
        
        for i in range(idx,len(nums)):
            if i>idx and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            arr.append(nums[i])
            self.ss(i+1,arr,nums,target-nums[i])
            arr.pop(-1)
            

        
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.ss(0,[],nums,target)
        return self.ans
        