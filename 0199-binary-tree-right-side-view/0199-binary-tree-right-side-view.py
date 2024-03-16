# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        answer = []
        
        def helper(node: TreeNode, level: int) -> None:
            if level == len(answer):
                answer.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
        
        helper(root, 0)
        return answer