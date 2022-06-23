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
            node, lo, hi = queue.popleft()
            if node.val <= lo or node.val >= hi:
                return False
            if node.left:
                queue.append((node.left, lo, node.val))
            if node.right:
                queue.append((node.right, node.val, hi))
        
        return True