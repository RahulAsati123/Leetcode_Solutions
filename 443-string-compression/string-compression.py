class Solution:
    def compress(self, chars: List[str]) -> int:
        arr = []
        ans = ""
        i = 0
        j = i+1
        count = 1
        while i<len(chars) and j<len(chars):
            if chars[i] == chars[j]:
                count+=1
                j+=1
            else:
                arr.append([chars[i],count])
                count = 1
                i = j
                j+=1
        arr.append([chars[i],count])
        for i in range(len(chars)):
            chars.pop()
        for i in range(len(arr)):
            ans+=arr[i][0]
            if arr[i][1] !=1:
                ans+=str(arr[i][1])
        for i in ans:
            chars.append(i)
        return len(chars)
        

            

       


       