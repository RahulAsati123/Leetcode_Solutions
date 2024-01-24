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
        
        if root.val not in self.m:
            self.m[root.val] =1
        else:
            self.m[root.val]+=1
        
        self.preorder(root.left)
        self.preorder(root.right)
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.m = {}
        ans = []
        self.preorder(root)
        print(self.m)
        for i in self.m.keys():
            if self.m[i] == max(list(self.m.values())):
                ans.append(i)
        return ans
        