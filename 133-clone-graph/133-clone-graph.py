"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        originalToClone = {}
        
        def clone(node):
            if node in originalToClone:
                return originalToClone[node]
            copy = Node(node.val)
            originalToClone[node] = copy
            if node.neighbors:
                copy.neighbors = [clone(n) for n in node.neighbors]
            return copy
        
        return clone(node)