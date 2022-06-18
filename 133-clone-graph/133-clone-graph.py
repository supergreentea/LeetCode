"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def clone(node):
            if not node:
                return None
            
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            
            oldToNew[node] = copy
            
            copy.neighbors = [clone(neighbor) for neighbor in node.neighbors]
            
            return copy
        
        return clone(node)