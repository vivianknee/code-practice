# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get numerical values of the linked lists
        # stored in reverse order
        digits1 = []
        digits2 = []
        head1, head2 = l1, l2

        while head1:
            digits1.insert(0, str(head1.val))
            head1 = head1.next
        
        while head2:
            digits2.insert(0, str(head2.val))
            head2 = head2.next

        # atp, we have two arrays of charaters of the digits in the linked lists
        num1 = int("".join(digits1))
        num2 = int("".join(digits2))
        sum = str(num1 + num2) # 9 7 5

        new_head = ListNode(sum[len(sum) -1]) # head val = 5
        curr = new_head

        for i in range(len(sum) -2 , -1, -1):
            curr.next = ListNode(sum[i])
            curr = curr.next
        
        return new_head
    