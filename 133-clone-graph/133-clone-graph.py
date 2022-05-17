"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.cloned = [None for _ in range(101)]
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        # node was already cloned
        if self.cloned[node.val]:
            return self.cloned[node.val]
        
        clone = Node(node.val)
        self.cloned[clone.val] = clone
        
        for nei in node.neighbors:
            clone.neighbors.append(self.cloneGraph(nei))
        
        return clone
        