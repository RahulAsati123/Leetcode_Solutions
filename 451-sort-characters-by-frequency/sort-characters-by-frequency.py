class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}
        arr = []
        res = ""
        ans = []
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
        for i in m.keys():
            arr.append(i)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if m[arr[i]]<m[arr[j]]:
                    arr[i],arr[j] = arr[j],arr[i]
        for i in arr:
            for j in range(m[i]):
                ans.append(i)
        for i in ans:
            res+=i
        return res
        
      
  