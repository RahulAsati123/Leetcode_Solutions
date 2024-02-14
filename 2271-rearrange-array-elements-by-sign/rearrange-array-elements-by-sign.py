class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        ans = []
        for i in range(len(nums)):
            if nums[i]>0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(arr1)):
            ans.append(arr1[i])
            ans.append(arr2[i])
        return ans
        
        