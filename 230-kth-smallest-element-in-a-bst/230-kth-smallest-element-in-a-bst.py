# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            if len(res) == k:
                return
            helper(root.right)
        
        helper(root)
        
        return res[k - 1]