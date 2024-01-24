# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root):
        if not root:
            return
        self.arr.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff = 10000000
        self.arr = []
        self.preorder(root)
        self.arr.sort()
        for i in range(len(self.arr)-1):
            if self.arr[i+1]-self.arr[i]<min_diff:
                min_diff = self.arr[i+1]-self.arr[i]
        return min_diff


        