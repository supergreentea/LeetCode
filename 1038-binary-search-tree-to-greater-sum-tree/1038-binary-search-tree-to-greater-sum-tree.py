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
        
        n = len(inorder_list)
        sums = [0] * n
        sums[-1] = inorder_list[-1].val
        for i in range(n - 2, -1, -1):
            sums[i] += inorder_list[i].val + sums[i + 1]
        
        for i in range(n):
            inorder_list[i].val = sums[i]
        
        return root
            
            