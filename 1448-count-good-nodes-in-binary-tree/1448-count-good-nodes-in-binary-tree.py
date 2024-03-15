# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        
        def dfs(node: TreeNode = root, maxSoFar: int = root.val):
            nonlocal good
            if node:
                if node.val >= maxSoFar:
                    good += 1
                    dfs(node.left, node.val)
                    dfs(node.right, node.val)
                else:
                    dfs(node.left, maxSoFar)
                    dfs(node.right, maxSoFar)
        
        dfs()
        return good