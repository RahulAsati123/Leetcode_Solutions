# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,count):
        if not root:
            return 
        
        count +=1
        if not root.left and not root.right:
            self.arr.append(count)
            count = 0
        self.preorder(root.left,count)
        self.preorder(root.right,count)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.preorder(root,0)
        self.arr.sort()
        if len(self.arr)==0:
            return 0
        return self.arr[0]



        