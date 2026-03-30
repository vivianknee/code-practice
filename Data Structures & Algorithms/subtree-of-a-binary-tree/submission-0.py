# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # bfs to find potential nodes to start tree comparison
        def bfs(root, subRoot):
            candidates = []  # return a list, not just one node
            
            if not root:
                return candidates
            
            queue = deque([root])

            while queue:
                node = queue.popleft()

                if node.val == subRoot.val:  
                    candidates.append(node)
                
                # always keep searching (remove the else)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            return candidates
        
        def isSameTree(p, q): # p and q represent nodes
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        candidates = bfs(root, subRoot)
        for node in candidates:
            if isSameTree(node, subRoot):
                return True
        
        return False                
        

        