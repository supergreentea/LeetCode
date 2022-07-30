"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def flatten_and_get_tail(node = head):
            if not node:
                return None
            
            tail = cur = node
            while cur:
                nxt = cur.next
                if not nxt:
                    tail = cur
                if cur.child:
                    # get tail
                    child_tail = flatten_and_get_tail(cur.child)
                    
                    # link to child
                    cur.next = cur.child
                    cur.child.prev = cur
                    
                    # connect tail with next node
                    child_tail.next = nxt
                    if nxt:
                        nxt.prev = child_tail
                    
                    cur.child = None
                cur = nxt if nxt else cur.next
            return tail
        
        flatten_and_get_tail()
        return head