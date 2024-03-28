# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node: TreeNode = root, level = 0):
            if not node:
                return
            if level == len(ans):
                ans.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level + 1)
        
        dfs()
        return ans