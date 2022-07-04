# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev, cur = None, node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt
            return prev
    
        r1 = reverse(l1)
        r2 = reverse(l2)
        
        carry = 0
        
        prev = None
        
        while r1 and r2:
            Sum = r1.val + r2.val
            Sum += carry
            if Sum >= 10:
                carry = 1
                Sum %= 10
            else:
                carry = 0
            new_node = ListNode(Sum)
            new_node.next = prev
            prev = new_node
            r1, r2 = r1.next, r2.next
        
        while r1:
            Sum = r1.val + carry
            if Sum >= 10:
                carry = 1
                Sum %= 10
            else:
                carry = 0
            new_node = ListNode(Sum)
            new_node.next = prev
            prev = new_node
            r1 = r1.next
        
        while r2:
            Sum = r2.val + carry
            if Sum >= 10:
                carry = 1
                Sum %= 10
            else:
                carry = 0
            new_node = ListNode(Sum)
            new_node.next = prev
            prev = new_node
            r2 = r2.next
        
        if carry:
            new_node = ListNode(1)
            new_node.next = prev
            prev = new_node
        
        return prev
        
        
        