# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root left right
        res = []
        
        def dfs(node):
            nonlocal res
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        
        dfs(root)
        return res