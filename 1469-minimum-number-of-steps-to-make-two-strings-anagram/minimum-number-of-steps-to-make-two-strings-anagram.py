class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        m = {}
        for i in s:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for i in t:
            if i not in m or m[i]==0:
                count+=1
            else:
                m[i]-=1
        return count

        