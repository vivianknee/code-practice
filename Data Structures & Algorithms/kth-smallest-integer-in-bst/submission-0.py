# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        # use in order traversal to get the list in order
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        print(self.res)
        return self.res[k - 1]