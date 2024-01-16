class Solution:
    def ss(self,nums,arr,target,idx):
        if idx == len(nums):
            if target == 0 :
                print(arr)
                self.ans.append(arr.copy())
                print(self.ans)
            return
       
        if nums[idx]<=target:
         
            arr.append(nums[idx])
          
            self.ss(nums,arr,target-nums[idx],idx)
      
            arr.pop(-1)
        
        self.ss(nums,arr,target,idx+1)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        arr = []
        self.ss(nums,arr,target,0)
        return self.ans
        