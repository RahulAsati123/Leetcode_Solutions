class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        m = {}
        ans = 0
        for i in nums:
            if i not in m:
                m[i] =1 
            else:
                m[i]+=1
        for i in m.keys():
            if m[i]==1:
                ans+= i
        return ans

        