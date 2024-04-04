class Solution:
    def maxDepth(self, s: str) -> int:
        ans = []
        current = 0
        op= "("
        cl = ")"
        for i in s:
            if i == op:
                current+=1
                ans.append(current)
            
            elif i == cl:
                current-=1
        if len(ans) == 0:
            return 0

        return max(ans)