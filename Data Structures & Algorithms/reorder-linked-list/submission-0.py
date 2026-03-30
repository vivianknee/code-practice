# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # atp fast has reached the end and slow is at the midpoint. 
        # reverse from slow to null now
        second = slow.next      # start of second half
        slow.next = None        # split the list
        prev = None

        while second:
            tmp = second.next   # save next node
            second.next = prev  # reverse the pointer
            prev = second       # move prev forward
            second = tmp 
        
        # merge the reversed list and the first half
        first = head #0
        second = prev #6

        while first and second:
            temp = second.next # temp = 6 --> 5 == 5
            second.next = first.next #6 --> 1
            first.next = second # 0 --> 6 --> 1

            first = second.next # 0 => 1
            second = temp # 5


        