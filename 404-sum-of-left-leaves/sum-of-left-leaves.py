# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root,isLeft):
        if not root:
            return 
        if root.left == None and root.right == None and isLeft == True:
            self.arr.append(root.val)
        self.preorder(root.left,True)
        self.preorder(root.right,False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.preorder(root,False)
        print(self.arr)
        return sum(self.arr)
        