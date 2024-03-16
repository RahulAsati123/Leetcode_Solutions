class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = []
        m = {0:-1}
        summ = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                summ -=1
            else:
                summ +=1
            if summ in m:
                ans.append(i-m[summ])
            else:
                m[summ] = i
        if len(ans)==0:
            return 0
        return max(ans)



        

        