# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        # top to bottom, so no dfs
        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.right and node.left: # right nodes always seen from right
                    queue.append(node.left)
                    queue.append(node.right)
                if not node.right and node.left: # no right and left on that level
                    queue.append(node.left)
                if not node.left and node.right:
                    queue.append(node.right)
            
            res.append(level[-1])
          
        return res
            
                
                
