# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = cur = ListNode(0)
        
        while l1 or l2:
            l1_val = l1.val if l1 else math.inf
            l2_val = l2.val if l2 else math.inf
            
            if l1_val < l2_val:
                cur.next = ListNode(l1_val)
                l1 = l1.next if l1 else None
            else:
                cur.next = ListNode(l2_val)
                l2 = l2.next if l2 else None
            cur = cur.next
        
        return prehead.next