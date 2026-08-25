# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        
        count = 0

        curr = head
        while curr != None:
            count+=1
            curr=curr.next

        count = count - n
        print(count)

        prev = dummy
        curr = head

        while count != 0 :
            count-=1
            prev=curr
            curr=curr.next

        prev.next = curr.next

        return dummy.next

        