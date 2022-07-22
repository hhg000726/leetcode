# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        g = []
        while head:
            if head.val < x:
                l.append(head.val)
            else:
                g.append(head.val)
            head = head.next
        if l:
            t = ListNode(l.pop(0))
            head = t
        elif g:
            t = ListNode(g.pop(0))
            head = t
        else:
            return None
        while l:
            n = ListNode(l.pop(0))
            t.next = n
            t = t.next
        while g:
            n = ListNode(g.pop(0))
            t.next = n
            t = t.next
        return head