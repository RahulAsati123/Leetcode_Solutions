# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def is_pseudo_palindrome(path):
            # Check if at most one digit has an odd frequency
            odd_count = 0
            for count in path.values():
                if count % 2 == 1:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(node, path):
            if not node:
                return

            path[node.val] += 1  # Add the current node to the path

            if not node.left and not node.right:  # Check if leaf node
                if is_pseudo_palindrome(path):
                    self.result += 1

            # Explore left and right subtrees
            dfs(node.left, path.copy())
            dfs(node.right, path.copy())

        self.result = 0
        dfs(root, defaultdict(int))
        return self.result
