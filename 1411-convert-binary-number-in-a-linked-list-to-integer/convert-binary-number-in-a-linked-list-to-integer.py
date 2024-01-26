# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = ""
        current = head
        while current:
            ans+= str(current.val)
            current = current.next
        return int(ans,2)

        