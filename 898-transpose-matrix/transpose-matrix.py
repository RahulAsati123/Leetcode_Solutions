class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        ans = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            ans.append(arr)
            arr = []
        return ans
        
        
        