# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # any other case
        dummy = ListNode(0, head)
        group_prev = dummy
        curr = head
        while length >= k:
            group_first = curr
            prev = None
            for i in range(k):  
                temp = curr.next 
                curr.next = prev  
                prev = curr 
                curr = temp  
            length -= k 

            group_prev.next = prev     #updated the head 
            group_first.next = curr   #updated where we start
            
            group_prev = group_first #move the prev to the start for next iteration

        return dummy.next
        
        
            


        
