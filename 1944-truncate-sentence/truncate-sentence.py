class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space = 0
        ans = ""
        for i in range(len(s)):
            if s[i] == " ":
                space+=1
            if space == k:
                break
           
            ans+=s[i]
        return ans
        
        