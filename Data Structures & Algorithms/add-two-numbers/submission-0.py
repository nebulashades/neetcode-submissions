# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c = 0

        p1 = l1
        p2 = l2

        head = curr = ListNode()

        while p1 and p2:
            s = (p1.val + p2.val + c) % 10
            c = (p1.val + p2.val + c) // 10

            new = ListNode(s)
            curr.next = new
            curr = curr.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            s = (p1.val + c) % 10
            c = (p1.val + c) // 10
            new = ListNode(s)
            curr.next = new
            curr = curr.next
            p1 = p1.next

        while p2:
            s = (p2.val + c) % 10
            c = (p2.val + c) // 10

            new = ListNode(s)
            curr.next = new
            curr = curr.next
            p2 = p2.next

        if c:
            new = ListNode(c)
            curr.next = new
            curr = curr.next

        return head.next
