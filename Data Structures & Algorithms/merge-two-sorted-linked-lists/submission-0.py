# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        p1 = list1
        p2 = list2
        dummy = ListNode()
        curr=dummy

        while p1 !=None and p2 !=None:
            if p1.val < p2.val:
                curr.next = p1
                curr=curr.next
                p1=p1.next
            else:
                curr.next=p2
                curr=curr.next
                p2=p2.next

        if p2:
            curr.next = p2
        else:
            curr.next = p1

        return dummy.next
            



         
        