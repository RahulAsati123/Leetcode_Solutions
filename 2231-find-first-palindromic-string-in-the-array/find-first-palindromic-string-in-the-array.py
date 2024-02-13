class Solution:
    def p(self,s):
        s1 = s[::-1]
        if s==s1:
            return True
        return False
            
    def isPalindrome(self,s):
        for i in range(len(s)):
            if s[i]!= s[len(s)-i-1]:
                return False
        return True

    def firstPalindrome(self, ords: List[str]) -> str:
        for i in ords:
            if self.p(i):
                return i
        return ""
        