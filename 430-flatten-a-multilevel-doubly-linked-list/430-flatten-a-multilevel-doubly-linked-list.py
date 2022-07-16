"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""
For nodes in list, if node has child, then flatten the child first.

Then node.next = flatten(child)
and the child's tail should point to original node.next.

Get the tail of the flattened child node.

Have it point to the next node.

The problem is we need access to flattened list's tail to point it
to the next node.

Can we keep a pointer to the tail as we flatten the list.

Case case for recursion: a child with no children.



"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def get_flattened_tail(node):
            if not node:
                return node
            tail = cur = node
            while cur:
                nxt = cur.next
                if not nxt:
                    tail = cur
                if cur.child:
                    # get tail
                    child_tail = get_flattened_tail(cur.child)
                    
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
        
        get_flattened_tail(head)
        return head
                
        
        
        