# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prehead = ListNode(-1, head)
        
        newTail = head.next
        newHead = self.reverseList(head.next)
        
        prehead.next = newHead
        newTail.next = head
        head.next = None
        
        return prehead.next
        
        
        