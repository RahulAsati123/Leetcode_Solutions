# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head
        if s.next == None:
            return s
        if f.next.next == None:
            return f.next
        while f.next.next:
            print(f)
            s = s.next
            f = f.next.next
            if f.next == None:
                break
            elif f.next.next == None:
                s = s.next
                break
        return s
        # count  = 0
        
        # current = head
        # while current:
        #     count+=1
        #     current = current.next
        
        # ans = 0
        # l = head
        # while ans!= count//2:
        #     l = l.next
        #     ans+=1
        # return l