# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        t = head
        ohead = head
        l = 0
        while t:
            t = t.next
            l += 1
        k = k % l
        if l == k or l == 1 or k == 0:
            return head
        for _ in range(l - k):
            head = head.next
        t = head
        for _ in range(k - 1):
            t = t.next
        t.next = ohead
        for _ in range(l - k):
            t = t.next
        t.next = None
        return head