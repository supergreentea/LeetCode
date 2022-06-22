# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorder_list = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder_list.append(root)
            inorder(root.right)
        
        inorder(root)
        
        suffix_sums = [0] * len(inorder_list)
        suffix_sums[-1] = inorder_list[-1].val
        for i in range(len(suffix_sums) - 2, -1 , -1):
            suffix_sums[i] = suffix_sums[i + 1] + inorder_list[i].val
        
        for i in range(len(inorder_list)):
            inorder_list[i].val = suffix_sums[i]
        
        return root
        