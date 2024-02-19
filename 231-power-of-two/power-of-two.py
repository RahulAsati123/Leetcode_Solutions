class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        binary = bin(n)
        s = str(binary)
        if (s.count("1") == 1):
            return True
        return False
