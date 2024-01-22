# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        arr = []
        while current.next:
            arr.append(current.val)
            current = current.next
        arr.append(current.val)
        for i in range(len(arr)//2):
            if arr[i]!=arr[len(arr)-i-1]:
                return False
        return True

        
       

        