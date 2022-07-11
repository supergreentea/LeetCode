# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def traverse(node, depth):
            if not node:
                return
            
            if len(ans) == depth:
                ans.append(node.val)
            
            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)
        
        traverse(root, 0)
        return ans