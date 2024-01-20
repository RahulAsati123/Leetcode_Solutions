class Solution:
    def topKFrequent(self, s: List[str], k: int) -> List[str]:
        m = {}
        ans = []
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
        arr = list(m.keys())
        arr.sort()
        arr.reverse()
        print(arr)
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if m[arr[i]] < m[arr[j]]:
                    arr[i],arr[j] = arr[j],arr[i]
                elif m[arr[i]] == m[arr[j]]:
                    arr[i],arr[j] = arr[j],arr[i]
    
        for i in range(k):
            ans.append(arr[i])
        return ans