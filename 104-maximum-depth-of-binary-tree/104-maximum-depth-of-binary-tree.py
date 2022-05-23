class Solution:
    def maxDepth(self, root):
        stack, depth = [], 0
        if not root:
            return depth
        stack.append((1, root))
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth