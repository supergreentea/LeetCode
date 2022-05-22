# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
    
        head = pointer = ListNode(0)
        heap = []

        for l in lists:
            cur = l
            while cur:
                heapq.heappush(heap, Wrapper(cur))
                cur = cur.next

        while len(heap) > 0:
            node = heapq.heappop(heap).node
            pointer.next = node
            pointer = pointer.next
        pointer.next = None
        return head.next
    
    
    