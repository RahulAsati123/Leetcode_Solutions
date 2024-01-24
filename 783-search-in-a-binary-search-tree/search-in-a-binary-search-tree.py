# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:



    def preorder(self,root,v):
        if not root:
            return 
        
        if root.val == v:
            self.ans = root
            return

        if root.val>v:
            self.preorder(root.left,v)
        else:
            self.preorder(root.right,v)

      
        
        
        
        
    def searchBST(self, root: Optional[TreeNode], v: int) -> Optional[TreeNode]:
        self.ans = None
        self.preorder(root,v)
        return self.ans


        