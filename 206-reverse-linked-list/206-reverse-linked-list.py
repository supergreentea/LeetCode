# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            # save pointer to next node
            nxt = cur.next
            
            # reverse pointer for current node
            cur.next = prev
            
            # move pointers
            prev, cur = cur, nxt
        
        # since cur is None, prev would be last node to be reversed, so head of reversed list
        return prev