# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root, -math.inf, math.inf)])
        while queue:
            root, lower, upper = queue.popleft()
            val = root.val
            if val <= lower or val >= upper:
                return False
            if root.right:
                queue.append((root.right, val, upper))
            if root.left:
                queue.append((root.left, lower, val))
        return True