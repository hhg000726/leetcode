# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        n1 = 0
        while 1:
            n1 += l1.val * 10 ** x
            x += 1
            if l1.next:
                l1 = l1.next
            else:
                break
        x = 0
        n2 = 0
        while 1:
            n2 += l2.val * 10 ** x
            x += 1
            if l2.next:
                l2 = l2.next
            else:
                break
        a = str(n1 + n2)
        ans = ListNode()
        ans.val = int(a[-1])
        b = ans
        for i in a[-2::-1]:
            t = ListNode()
            t.val = int(i)
            t.next = None
            b.next = t
            b = t
        return ans