# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        if not root:
            return good
        
        def dfs(node: TreeNode = root, maxSoFar: int = root.val) -> None:
            nonlocal good
            if node:
                if node.val >= maxSoFar:
                    good += 1
                    maxSoFar = node.val
                for child in [node.left, node.right]:
                    dfs(child, maxSoFar)
        
        dfs()
        return good