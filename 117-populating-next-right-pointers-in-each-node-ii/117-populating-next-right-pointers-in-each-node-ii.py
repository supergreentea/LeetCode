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
    def connect(self, root: 'Node') -> 'Node':
        
        def process_child(child):
            nonlocal prev
            nonlocal leftmost
            if child:
                if prev:
                    prev.next = child
                else:
                    leftmost = child
                prev = child
        
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                process_child(curr.left)
                process_child(curr.right)
                curr = curr.next
        return root
        