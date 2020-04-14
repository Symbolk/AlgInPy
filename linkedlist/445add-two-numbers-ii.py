# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # key: find the prev node without reverting the linked list
    # reverse order --> stack: O(max(m, n)), O(m+n)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            cur = a + b + carry
            carry = cur // 10  # carry = 1 if cur >= 10 else 0
            cur %= 10
            node = ListNode(cur)
            # prepend
            node.next = ans
            ans = node

        return ans

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        # dummy node
        head = ListNode()
        carry = 0
        while s1 or s2 or carry != 0:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            cur = a + b + carry
            carry = cur // 10  # carry = 1 if cur >= 10 else 0
            cur %= 10
            node = ListNode(cur)
            # prepend
            node.next = head.next
            head.next = node

        return head.next
