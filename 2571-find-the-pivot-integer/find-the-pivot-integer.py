class Solution:
    def pivotInteger(self, n: int) -> int:
        s2 = n*(n+1)//2
        for i in range(1,n+1):
            s1 = i*(i+1)//2
            if 2*s1 == s2 + i:
                return i
        return -1
            
        