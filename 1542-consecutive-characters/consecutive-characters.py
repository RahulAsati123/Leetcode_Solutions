class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        j = 1
        max_count = 1
        count =1
        while i<len(s) and j<len(s):
            if s[i] == s[j]:
                count+=1
                j+=1
            else:
                if count>max_count:
                    max_count = count
                count = 1
                i= j
                j+=1
        if count>max_count:
            max_count = count
        return max_count
            

        