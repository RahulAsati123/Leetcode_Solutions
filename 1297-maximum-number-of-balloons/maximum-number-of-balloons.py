class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countb = text.count("b")
        counta = text.count("a")
        countl = text.count("l")
        counto = text.count("o")
        countn = text.count("n")
        return min([countb,counta,countl//2,counto//2,countn])
