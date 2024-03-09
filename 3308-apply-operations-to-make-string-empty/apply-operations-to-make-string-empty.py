class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        m = {}
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
        arr = []
        max_frequency = max(list(m.values()))

        s1 = ""
        for i in reversed(s):
            if m[i] == max_frequency and i not in s1:
                s1+= i
            
        return s1[::-1]


        