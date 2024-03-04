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
        
        if root.val!= self.uvalue:
            print(root.val)
            self.ans = False
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.uvalue = root.val
        self.preorder(root)
        return self.ans

        