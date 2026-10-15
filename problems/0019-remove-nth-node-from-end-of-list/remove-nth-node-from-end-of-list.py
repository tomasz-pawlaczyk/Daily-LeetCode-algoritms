class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current = head
        slow = None
        iteration = 1
        while current.next is not None:
            if iteration - n == 0:
                slow = head
            if iteration - n > 0:
                slow = slow.next
            current = current.next
            iteration += 1
            
        if iteration == n:
            head = head.next
        else:
            slow.next = slow.next.next
        return head


# WZORCOWE
# class Solution:
#     def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
#         dummy = ListNode(0, head)   # węzeł pomocniczy przed głową
#         fast = dummy
#         slow = dummy

#         for _ in range(n):          # fast ucieka o n kroków do przodu
#             fast = fast.next

#         while fast.next is not None:  # oba idą razem, aż fast stanie na ostatnim węźle
#             fast = fast.next
#             slow = slow.next

#         slow.next = slow.next.next  # slow stoi tuż przed węzłem do usunięcia
#         return dummy.next        