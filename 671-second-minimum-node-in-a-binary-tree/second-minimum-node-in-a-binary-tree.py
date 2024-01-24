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
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.preorder(root)
        box = list(set(self.arr))
        box.sort()
        print(box)
        if len(box)<2:
            return -1
        return box[1]


        