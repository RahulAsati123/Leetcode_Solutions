class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = {}
        ans = 0
        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        arr = list(m.values())
        for i in nums:
            if m[i] == max(arr):
                ans+=1
        return ans
       
            
        