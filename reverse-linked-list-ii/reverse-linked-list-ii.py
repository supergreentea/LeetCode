# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prehead = ListNode(0, head)
        
        pre_left, cur = prehead, head
        
        # move pointers so cur points to left
        for i in range(left - 1):
            nxt = cur.next
            pre_left, cur = cur, nxt
        
        # reverse from left to right (there are right - left + 1 nodes to reverse)
        prev = None
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        
        # cur is now pointing to after right
        pre_left.next.next = cur
        pre_left.next = prev
        
        return prehead.next