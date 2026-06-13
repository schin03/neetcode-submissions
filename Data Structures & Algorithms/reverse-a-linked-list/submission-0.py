# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        headPtr = head
        while headPtr is not None:
            l.append(headPtr.val)
            headPtr = headPtr.next
        
        l.reverse()
        n = 0
        headPtr = head
        while headPtr is not None:
            headPtr.val = l[n]
            n += 1
            headPtr = headPtr.next
        
        return head
