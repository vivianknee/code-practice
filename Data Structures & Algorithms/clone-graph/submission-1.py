"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}  # maps original node → cloned node
        
        def dfs(node):
            if node in old_to_new:
                # already cloned, return the clone
                return old_to_new[node]
            
            # create clone
            copy = Node(node.val)
            old_to_new[node] = copy
            
            # clone all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node)
        

              