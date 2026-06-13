# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: return False
        temp = head

        while head is not None:
            head = head.next
            if temp.next is None or temp.next.next is None: return False
            temp = temp.next
            temp = temp.next
            
            if head.val == temp.val:
                return True

        return False