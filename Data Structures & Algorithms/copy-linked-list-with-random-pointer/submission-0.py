"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        old_to_new = {}  # hash maps old node → new node
        
        # First pass: create all new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # second pass is assigning next and random
        curr = head
        while curr:
            # lookup is just the old node
            old_to_new[curr].next = old_to_new.get(curr.next) #get gets the new node
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new.get(head)