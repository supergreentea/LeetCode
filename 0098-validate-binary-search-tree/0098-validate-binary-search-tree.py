# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node: TreeNode = root, lowerBound: float = -math.inf, upperBound: float = math.inf):
            if not node:
                return True
            if node.val <= lowerBound or node.val >= upperBound:
                return False
            return validate(node.left, lowerBound, node.val) and validate(node.right, node.val, upperBound)
        
        return validate()