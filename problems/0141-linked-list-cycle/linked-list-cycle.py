# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        szybki = head
        wolny = head

        while szybki is not None and szybki.next is not None:
            szybki = szybki.next.next
            wolny = wolny.next
            if szybki is wolny:
                return True
        return False
        