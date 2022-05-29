# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
        
        dfs(root)
        return inorder[k - 1].val