# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if n == length:
            return head.next

        prev = head
        for i in range(length - n - 1): # gets the prev value before target
            prev = prev.next
        
        prev.next = prev.next.next

        return head
        
            
