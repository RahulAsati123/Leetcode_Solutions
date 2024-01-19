class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])

        # Initialize the dp array with infinity, and set the last row equal to the matrix's last row
        dp = [[float('inf')] * w for _ in range(h)]
        dp[-1] = matrix[-1]

        # Iterate from the second last row to the first row
        for i in range(h - 2, -1, -1):
            for j in range(w):
                # For each cell, calculate the minimum sum of the falling path up to that cell
                # It considers the current cell value and the minimum of the three possible
                # previous positions (directly below, diagonally left, and diagonally right)
                dp[i][j] = matrix[i][j] + min(
                    dp[i + 1][j],  # Directly below
                    dp[i + 1][j - 1] if j > 0 else float("inf"),  # Diagonally left
                    dp[i + 1][j + 1] if j < w - 1 else float("inf")  # Diagonally right
                )

        # The answer is the minimum value in the first row of dp
        return min(dp[0])