class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        m  = {}
        for i in nums:
            if i not in m and i%2 ==0:
                m[i] =1
            elif i in m:
                m[i]+=1

        if len(m)==0:
            return -1
        
        ans = []
        arr = list(m.values())
        arr.sort()
        for i in m.keys():
            if m[i] == arr[-1]:
                ans.append(i)
        return min(ans)
            
        