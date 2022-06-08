# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0
        
        def dfs(root, max_value):
            nonlocal good_nodes
            if not root:
                return
            if root.val >= max_value:
                good_nodes += 1
            new_max = max(max_value, root.val)
            dfs(root.left, new_max)
            dfs(root.right, new_max)
        
        dfs(root, -math.inf)
        return good_nodes