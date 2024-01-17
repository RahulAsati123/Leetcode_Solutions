class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for i in arr:
            if i not in m:
                m[i]= 1
            else:
                m[i]+=1
        arr = list(m.values())
        return len(arr) == len(set(arr))
        