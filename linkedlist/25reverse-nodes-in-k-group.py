# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n), O(1)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # reverse a given range (s, e)
        def reverse(s, e):
            pre, cur = s, s.next
            head = s.next
            while cur != e:
                cur.next, pre, cur = pre, cur, cur.next
            s.next = pre
            head.next = cur
            # head is now the end node of reversed linked list
            return head

        if head is None or k < 2:
            return head
        hair = ListNode(0)
        hair.next = head
        # (start, end]
        start, end = hair, head
        cnt = 0
        while end:
            cnt += 1
            if cnt % k == 0:
                start = reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        # hair always point to the first node
        return hair.next

    # with stack: O(n), O(k)
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        while True:
            cnt = k
            stack = []
            cur = head
            while cnt and cur:
                stack.append(cur)
                cur = cur.next
                cnt -= 1
            # less than k
            if cnt:
                pre.next = head
                break
            # reverse append
            while stack:
                pre.next = stack.pop()
                pre = pre.next
            # linked with other
            pre.next = cur
            head = cur
        return dummy.next

    # recursion: O(n), O(1)
    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        cur = head
        cnt = 0
        while cur and cnt != k:
            cur = cur.next
            cnt += 1
        if cnt == k:
            cur = self.reverseKGroup2(cur, k)
            while cnt:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                cnt -= 1
            head = cur
        return head
