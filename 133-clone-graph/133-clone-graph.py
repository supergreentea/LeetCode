"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        original_to_copy = {}
        
        def clone(node):
            if not node:
                return 
            
            if node in original_to_copy:
                return original_to_copy[node]
            
            copy = Node(node.val)
            
            original_to_copy[node] = copy
            
            copy.neighbors = [clone(neighbor) for neighbor in node.neighbors]
            
            return copy
        
        return clone(node)