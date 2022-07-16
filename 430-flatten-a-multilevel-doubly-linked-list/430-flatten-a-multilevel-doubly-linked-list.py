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
                # move to original next node if it exists, otherwise point to node below
                cur = nxt if nxt else cur.next
            return tail
        
        get_flattened_tail(head)
        return head