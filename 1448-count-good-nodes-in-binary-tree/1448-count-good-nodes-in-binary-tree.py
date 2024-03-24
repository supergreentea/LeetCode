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
            return 0
        
        def count(node: TreeNode = root, maxSoFar: int = root.val) -> None:
            if not node:
                return
            nonlocal good
            if node.val >= maxSoFar:
                good += 1
            maxSoFar = max(maxSoFar, node.val)
            count(node.left, maxSoFar)
            count(node.right, maxSoFar)
        
        count()
        return good