# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root):
        if not root:
            return 
        
        self.arr.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.arr = []
        self.preorder(root1)
        self.preorder(root2)
        self.arr.sort()
        return self.arr