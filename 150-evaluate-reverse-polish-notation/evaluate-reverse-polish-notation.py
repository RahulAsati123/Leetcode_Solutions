import math
class Solution:
    def solve(self,sign,a,b):
        a = int(a)
        b= int(b)
        if sign=="+":
            return a+b
        elif sign == "-":
            return b-a
        elif sign == "*":
            return b*a
        else:
            return int(b/a)
    def evalRPN(self, tokens: List[str]) -> int:
        sign = {"+","-","*","/"}
        ans = 0
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] not in sign:
                stack.append(tokens[i])
            else:
                a= stack.pop()
                b = stack.pop()
                stack.append(self.solve(tokens[i],a,b))
        return int(stack[0])
    
            

