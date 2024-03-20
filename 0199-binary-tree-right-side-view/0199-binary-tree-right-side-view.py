# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        
        def dfs(node: TreeNode, level: int) -> None:
            if level == len(answer):
                answer.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level + 1)
        
        dfs(root, 0)
        return answer