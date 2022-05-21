# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            val = root.val
            if val <= lower or val >= upper:
                return False
            if root.right:
                stack.append((root.right, val, upper))
            if root.left:
                stack.append((root.left, lower, val))
        return True