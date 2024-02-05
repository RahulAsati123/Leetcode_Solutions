class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = []
        q = ""
        map = {}
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        for i in map.keys():
            if map[i] ==1:
                q += i
                break
        for i in range(len(s)):
            if s[i] == q:
                return i
            
        return -1