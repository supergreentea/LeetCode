# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
        
        if not root:
            return False
        if not subRoot:
            return True
        
        return same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)