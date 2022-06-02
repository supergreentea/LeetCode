# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0
        
        def dfs(root, max_on_path):
            nonlocal good_nodes
            if not root:
                return 
            if root.val >= max_on_path:
                good_nodes += 1
            max_on_path = max(max_on_path, root.val)
            dfs(root.left, max_on_path)
            dfs(root.right, max_on_path)
        
        dfs(root, -math.inf)
        
        return good_nodes