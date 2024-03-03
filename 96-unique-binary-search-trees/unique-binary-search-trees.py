class Solution:
    def factorial(self,n):
        ans = 1
        for i in range(1,n+1):
            ans = ans*i
        return ans
    def numTrees(self, n: int) -> int:
        print(self.factorial(5))
        return (self.factorial(2*n)//(self.factorial(n)*self.factorial(n)*(n+1)))

        