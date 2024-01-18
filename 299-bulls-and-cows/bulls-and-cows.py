class Solution:
    def getHint(self, s: str, g: str) -> str:
        m = {}
        x= 0
        y = 0
        for i in s:
            if i not in m:
               m[i]=1
            else:
                m[i]+=1
        
        for i in range(len(g)):
            if g[i] in m and m[g[i]]>0 and g[i]==s[i]:
                x+=1
                m[g[i]]-=1
        
        for i in range(len(g)):
            if g[i] in m and m[g[i]]>0 and g[i]!=s[i]:
                y+=1
                m[g[i]]-=1
        return f"{x}A{y}B"






        