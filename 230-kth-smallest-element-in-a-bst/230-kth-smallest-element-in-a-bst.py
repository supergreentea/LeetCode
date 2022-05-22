# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if not root:
            return res
        cur = root
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            if len(res) == k:
                return res[k - 1]
            if node.right:
                cur = node.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return res[k - 1]