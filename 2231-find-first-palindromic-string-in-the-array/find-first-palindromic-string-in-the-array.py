class Solution:
    def isPalindrome(self,s):
        for i in range(len(s)):
            if s[i]!= s[len(s)-i-1]:
                return False
        return True
    def firstPalindrome(self, ords: List[str]) -> str:
        for i in ords:
            if self.isPalindrome(i):
                return i
        return ""
        