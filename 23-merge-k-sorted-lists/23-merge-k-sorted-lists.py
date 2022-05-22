# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        prehead = prev = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        nodes.sort()
        for val in nodes:
            prev.next = ListNode(val)
            prev = prev.next
        return prehead.next