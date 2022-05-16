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
        array = []
        prev = head
        while prev:
            array.append(prev)
            prev = prev.next
        res = []
        l, r = 0, len(array) - 1
        while l <= r:
            res.append(array[l])
            res.append(array[r])
            l += 1
            r -= 1
        prev = res[0]
        for i in range(1, len(res)):
            prev.next = res[i]
            prev = prev.next
        prev.next = None
        