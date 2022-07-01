"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        original_to_copy = {}
        
        cur = head
        while cur:
            original_to_copy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = original_to_copy[cur]
            copy.next = original_to_copy.get(cur.next, None)
            copy.random = original_to_copy.get(cur.random, None)
            cur = cur.next
        
        return original_to_copy[head]
            
        