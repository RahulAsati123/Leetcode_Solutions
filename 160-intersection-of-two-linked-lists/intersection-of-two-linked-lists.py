# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = {}
        current = headA
        while current:
            m[current] = current.val
            current = current.next
        
        current2 = headB
        while current2:
            if current2 in m:
                return current2
            current2 = current2.next
        return 
        
        

        