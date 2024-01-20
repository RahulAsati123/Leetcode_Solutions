
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        stack = []
        result = 0
        arr = [0] + arr + [0]
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                result += arr[j] * (i - j) * (j - stack[-1])
            stack.append(i)
        return result % (10**9 + 7)