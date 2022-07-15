# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        
        def dfs(root):
            nonlocal max_length
            
            if not root:
                return 0
            
            left_sequence = dfs(root.left) + 1
            right_sequence = dfs(root.right) + 1
            
            if root.left and root.left.val != root.val + 1:
                left_sequence = 1
            
            if root.right and root.right.val != root.val + 1:
                right_sequence = 1
            
            length = max(left_sequence, right_sequence)
            max_length = max(max_length, length)
            return length
        
        dfs(root)
        return max_length