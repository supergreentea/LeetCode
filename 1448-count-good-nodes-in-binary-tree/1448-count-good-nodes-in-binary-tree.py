# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        
        def dfs(node, cur_max):
            nonlocal good_nodes
            if not node:
                return 
            if node.val >= cur_max:
                good_nodes += 1
            new_max = max(cur_max, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        
        dfs(root, -math.inf)
        return good_nodes