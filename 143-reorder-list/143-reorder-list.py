# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow now points to middle node
        
        # reverse second half
        prev, cur = None, slow
        while cur:
            # store pointer to next node
            nxt = cur.next
            # reverse pointer for cur node
            cur.next = prev
            # shift pointers
            prev, cur = cur, nxt
        # prev now head of reversed half
        
        # merge halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        return head