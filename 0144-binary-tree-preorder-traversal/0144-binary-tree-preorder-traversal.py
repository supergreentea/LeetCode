# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def preorder(node: TreeNode = root) -> None:
            if node:
                ans.append(node.val)
                for child in [node.left, node.right]:
                    preorder(child)
        
        preorder()
        return ans