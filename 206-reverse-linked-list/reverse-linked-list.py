# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize three pointers
        prev = None
        current = head
        next_node = None

        # Traverse the list
        while current is not None:
            # Save the next node
            next_node = current.next
            
            # Reverse the direction of the pointer
            current.next = prev
            
            # Move pointers one step forward
            prev = current
            current = next_node

        # The new head is the previous node
        return prev
