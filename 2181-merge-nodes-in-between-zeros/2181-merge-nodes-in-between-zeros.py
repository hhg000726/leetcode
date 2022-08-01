# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = ListNode(0, head)
        while t:
            if t.next.next:
                if t.next.val != 0 and t.next.next.val != 0:
                    t.next.val += t.next.next.val
                    t.next.next = t.next.next.next
                else:
                    t = t.next
            else:
                break
        t = ListNode(0, head)
        while t:
            if t.next and t.next.val == 0:
                t.next = t.next.next
            else:
                t = t.next
        if head.val == 0:
            return head.next
        else:
            return head