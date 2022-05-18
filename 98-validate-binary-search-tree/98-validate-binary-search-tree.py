# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, left, right):
            if not root:
                return True
            if left >= root.val or right <= root.val:
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        
        return helper(root, float('-inf'), float('inf'))