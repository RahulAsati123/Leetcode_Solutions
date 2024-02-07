class Solution:
    def gcd(self,n1,n2):
        ans = 1
        for i in range(1,min(n1,n2)+1):
            if n1%i == 0 and n2%i ==0:
                if i>ans:
                    ans = i
        return ans

    def canMeasureWater(self, j1: int, j2: int, target: int) -> bool:
        if j1+j2 < target:
            return False
        elif j1 == target or j2 == target:
            return True
        k = self.gcd(j1,j2)
        if target%k ==0:
            return True
        return False
        