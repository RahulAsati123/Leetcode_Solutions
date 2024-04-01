class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # Method 1 : 
        arr = s.split()
        ans = arr[len(arr)-1]
        return len(ans)

        # Method 2:
        # count = 0
        # s1 = s[::-1]
        # print(s1)
        # for i in range(len(s1)):
        #     print(s1[i])
        #     if s1[i] == " ":
        #         if count !=0:
        #             break
        #     else:
        #         count+=1
        # return count