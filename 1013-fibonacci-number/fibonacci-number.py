class Solution:
    def solve(self,n,dp):
        if n==0:
            return 0
        if n == 1 or n==2:
            return 1
        if dp[n]!=-1:
            return dp[n]
        left = self.solve(n-1,dp)
        right = self.solve(n-2,dp)
        dp[n] = left+right
        return dp[n]
        
    
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.solve(n,dp)
        
        
        