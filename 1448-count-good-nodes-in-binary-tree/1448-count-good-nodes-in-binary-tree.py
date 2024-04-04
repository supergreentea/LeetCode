# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        
        def count(node: TreeNode = root, maxSoFar: int = -math.inf) -> None:
            nonlocal good
            if not node:
                return
            if node.val >= maxSoFar:
                good += 1
            for child in [node.left, node.right]:
                count(child, max(maxSoFar, node.val))
        
        count()
        return good