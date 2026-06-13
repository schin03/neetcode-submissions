# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: return False
        temp = head

        while temp and temp.next:
            temp = temp.next.next
            head = head.next
            if temp == head: return True

        return False