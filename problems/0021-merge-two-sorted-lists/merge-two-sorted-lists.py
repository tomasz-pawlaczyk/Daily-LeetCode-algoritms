# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        aktualny = ListNode()
        start = aktualny

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                aktualny.next = list1
                list1 = list1.next
            else:
                aktualny.next = list2
                list2 = list2.next
                
            aktualny = aktualny.next

        if list1 is None:
            aktualny.next = list2
        else:
            aktualny.next = list1

        return start.next


        