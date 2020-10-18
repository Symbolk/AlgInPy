# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(L), O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getlen(node):
            l = 0
            while node:
                l += 1
                node = node.next
            return l

        dummy = ListNode(0, head)
        l = getlen(head)
        cur = dummy

        for i in range(1, l - n + 1):
            cur = cur.next
        cur.next = cur.next.next

        # not return head since head may be deleted!
        return dummy.next

    # stack: O(L), O(L)
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    # double pointers: O(L), O(1)
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        i, j = head, dummy
        for _ in range(n):
            i = i.next
        while i:
            i = i.next
            j = j.next

        j.next = j.next.next
        return dummy.next
