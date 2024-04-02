class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s)!= len(t):
        #     return False
        # map = {}
        # map1 = {}
        # for i in range(len(s)):
        #     if s[i] not in map:
        #         map[s[i]] = t[i]
        #     else:
        #         if (map[s[i]] == t[i]):
        #             continue
        #         else:
        #             return False
        
        
        # return True

        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = t[i]
            else:
                if m[s[i]] != t[i]:
                    return False

        box = set(m.values())
        if len(box)!= len(m.values()):
            return False
        return True

        
        