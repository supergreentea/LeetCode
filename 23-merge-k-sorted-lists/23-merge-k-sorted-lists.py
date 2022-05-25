# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def mergeTwoLists(p, q):
            head = pointer = ListNode(0)
            while p and q:
                if p.val < q.val:
                    pointer.next = p
                    p = p.next
                else:
                    pointer.next = q
                    q = q.next
                pointer = pointer.next
            pointer.next = p if p else q
            return head.next
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                p = lists[i]
                q = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(mergeTwoLists(p, q))
            lists = merged_lists
            
        return lists[0]
        