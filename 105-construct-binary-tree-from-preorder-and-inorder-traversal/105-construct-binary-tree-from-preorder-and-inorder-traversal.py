# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # root, left, right
        m = inorder.index(preorder[0]) # m - 1 elements in left subtree
        
        root.left = self.buildTree(preorder[1 : m + 1], inorder[:m])
        root.right = self.buildTree(preorder[m + 1:], inorder[m + 1:])
        return root