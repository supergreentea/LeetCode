"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    def process_child(self, child, prev, leftmost):
        if child:
            if prev:
                prev.next = child
            else:
                leftmost = child
            prev = child
        return prev, leftmost
        
        
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
    
        leftmost = root
        
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                
                curr = curr.next
        
        return root