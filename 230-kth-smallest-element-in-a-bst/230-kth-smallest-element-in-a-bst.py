# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while stack or cur:
            # go left as much as possible
            while cur:
                stack.append(cur)
                cur = cur.left
            k -= 1
            cur = stack.pop()
            if k == 0: # we visited k nodes, so current node is kth smallest
                return cur.val
            cur = cur.right # visit right subtree