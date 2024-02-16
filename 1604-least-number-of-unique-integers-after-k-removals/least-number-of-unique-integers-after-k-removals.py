class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for a in arr:
            if a in dic.keys():
                dic[a]+=1
            else: dic[a]=1
        heap = list(dic.values())
        heapq.heapify(heap)
        
        res = len(heap)
        while k>0 and heap:
            f = heapq.heappop(heap)
            if k>=f:
                k-=f
                res -=1
        return res