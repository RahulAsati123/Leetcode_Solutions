class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        m = {}
        i = 0
        ans = []
        while i<len(s):
            if s[i:i+10] not in m:
                m[s[i:i+10]] = 1
                i+=1
            else:
                m[s[i:i+10]] +=1
                i+=1
        print(m)
        for i in m.keys():
            if m[i]>1:
                ans.append(i)
        return ans


        