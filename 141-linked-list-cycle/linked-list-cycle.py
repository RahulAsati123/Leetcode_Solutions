# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head 
        m = {}
        if not current:
            return False
        
        while current.next:
            if current not in m:
                m[current] = current.val
                current = current.next
            else:
                return True
        return False
            
              
        