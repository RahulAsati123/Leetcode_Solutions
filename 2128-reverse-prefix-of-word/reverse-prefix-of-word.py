class Solution:
    def reversePrefix(self, s: str, ch: str) -> str:
        temp = 0
        for i in range(len(s)):
            if s[i] == ch:
                temp+=i
                break
        ans = ""
        for i in range(temp,-1,-1):
            ans+= s[i]
        for i in range(temp+1,len(s)):
            ans += s[i]
        return ans
