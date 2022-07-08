# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode()
        answer = a
        while list1 or list2:
            if list1:
                if list2:
                    if list1.val > list2.val:
                        t = ListNode(list2.val, None)
                        list2 = list2.next
                    else:
                        t = ListNode(list1.val, None)
                        list1 = list1.next
                else:
                    t = ListNode(list1.val, None)
                    list1 = list1.next
            else:
                t = ListNode(list2.val, None)
                list2 = list2.next
            a.next = t
            a = a.next
        return answer.next