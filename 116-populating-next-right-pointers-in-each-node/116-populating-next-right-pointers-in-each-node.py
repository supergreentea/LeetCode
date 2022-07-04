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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = deque([root])
        while queue:
            n = len(queue)
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            for _ in range(n - 1):
                next_node = queue.popleft()
                if next_node.left:
                    queue.append(next_node.left)
                if next_node.right:
                    queue.append(next_node.right)
                node.next = next_node
                node = next_node
            node.next = None
            
        return root