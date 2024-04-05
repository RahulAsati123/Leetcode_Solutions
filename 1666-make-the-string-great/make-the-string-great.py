class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack)!=0 and abs(ord(i)-ord(stack[-1])) == 32:
                stack.pop(-1)
            else:
                stack.append(i)
        return "".join(stack)

        