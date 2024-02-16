class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for a in arr:
            if a in dic.keys():
                dic[a]+=1
            else: dic[a]=1
        l = sorted(list(dic.values()))
        while k>0:
            k = k - l[0]
            l.pop(0)
        if k==0: return len(l)
        else: return len(l)+1