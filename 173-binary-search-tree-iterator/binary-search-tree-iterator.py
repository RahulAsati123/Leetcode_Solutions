# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self,root):
        if not root:
            return 
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.inorder(root)
        self.i = 0
        

    def next(self) -> int:
        return_value =  self.arr[self.i]
        self.i +=1
        return return_value
        
    def hasNext(self) -> bool:
        if self.i< len(self.arr):
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()