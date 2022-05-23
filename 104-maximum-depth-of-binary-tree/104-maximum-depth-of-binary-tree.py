class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        depth, stack = 0, [(root, 1)]
        while stack:
            root, cur_depth = stack.pop()
            if root:
                depth = max(depth, cur_depth)
                stack.append((root.left, cur_depth + 1))
                stack.append((root.right, cur_depth + 1))
        return depth