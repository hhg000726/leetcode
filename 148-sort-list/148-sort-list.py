# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        t = ListNode(l.pop(0))
        head = t
        while l:
            a = ListNode(l.pop(0))
            t.next = a
            t = a
        return head