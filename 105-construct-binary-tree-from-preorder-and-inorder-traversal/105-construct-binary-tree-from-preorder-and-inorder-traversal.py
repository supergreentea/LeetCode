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
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        elements_in_left_subtree = inorder.index(root_val)
        
        root.left = self.buildTree(preorder[1 : elements_in_left_subtree + 1], inorder[:elements_in_left_subtree])
        root.right = self.buildTree(preorder[elements_in_left_subtree + 1 :], inorder[elements_in_left_subtree + 1:])
        return root