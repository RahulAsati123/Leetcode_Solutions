class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = (n*(n+1))//2
        # map = {}
        # for i in nums:
        #     if i not in map:
        #         map[i] =1
        #     else:
        #         map[i]+=1
        # for i in map:
        #     if map[i] ==2:
        #         nu = i
        
        # nums.remove(nu)
        # ans1 = ans-sum(nums)
        # return [nu,ans1]

        n = len(nums)
        sum_of_n = n*(n+1)//2
        box = set()
        for i in nums:
            if i not in box:
                box.add(i)
            else:
                a1 = i
                break
        arr = list(set(nums))
        a2 = sum_of_n - sum(arr)
        return [a1,a2]


       

