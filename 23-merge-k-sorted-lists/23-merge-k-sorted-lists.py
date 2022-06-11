# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(p, q):
            cur = prehead = ListNode(0)
            while p and q:
                if p.val < q.val:
                    cur.next = p
                    p = p.next
                else:
                    cur.next = q
                    q = q.next
                cur = cur.next
            cur.next = p if p else q
            return prehead.next
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                p = lists[i]
                q = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge(p, q))
            lists = merged_lists
        
        return lists[0]