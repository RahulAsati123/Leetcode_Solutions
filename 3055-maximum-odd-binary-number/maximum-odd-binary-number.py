class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count("1")
        ans = ""
        arr = []
        for i in range(len(s)-1):
            if count>1:
                arr.append("1")
                count-=1
            else:
                arr.append("0")
        arr.append("1")
        for i in arr:
            ans+=i
        return ans
       
        
        