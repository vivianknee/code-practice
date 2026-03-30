# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, min_val, max_val): 
            if not curr:
                return True

            if curr.val <= min_val or curr.val >= max_val:
                return False

            left = dfs(curr.left, min_val, curr.val)
            right = dfs(curr.right, curr.val, max_val)

            return left and right
        
        return dfs(root, float('-inf'), float('inf'))

            