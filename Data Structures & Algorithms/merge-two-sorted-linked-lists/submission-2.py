# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None: 
            return list1
        
        head = list1
        
        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            list1 = list1.next
        curr = head
        while curr is not None:

            if list1 is None:
                curr.next = list2
                curr = list2
                break
            if list2 is None:
                curr.next = list1
                curr = list1
                break
            if list1.val > list2.val:
                temp = list2.next
                curr.next = list2
                curr = list2
                list2 = list2.next
            else:
                temp = list1.next
                curr.next = list1
                curr = list1
                list1 = list1.next
                
        return head

        