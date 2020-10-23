# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # recursion: O(n), O(n) (notice that space is still O(n) for recursion stack)
    # the deepest recursion is the last node of linkedlist
    def isPalindrome(self, head: ListNode) -> bool:
        # make global
        self.front = head

        # useless
        def print_val(cur):
            if not cur:
                return
            print_val(cur.next)
            print(cur.val)

        def recurCheck(cur):
            if cur:
                if not recurCheck(cur.next):
                    return False
                if self.front.val != cur.val:
                    return False
                self.front = self.front.next
            return True

        return recurCheck(head)

    # the key problem of single linkedlist is backward
    # so use stack: O(n), O(n)
    def isPalindrome1(self, head: ListNode) -> bool:
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.val != stack.pop():
                return False
            cur = cur.next
        return len(stack) == 0

    # find mid and reverse latter half
    # O(n), O(1)
    # remember to restore the linkedlist after
    def isPalindrome2(self, head: ListNode) -> bool:
        if not head:
            return True

        def findmid(node):
            slow = fast = node
            # while fast and fast.next:
            # !notice here!
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            # slow is the end of left half (length=even)
            # slow is the center of list (length=odd)
            return slow

        def reverse(node):
            pre, cur = None, node
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre

        mid = findmid(head)
        tmp = mid.next
        res = True

        # right end
        r = reverse(mid.next)
        # left end
        l = head

        while res and r:
            if l.val != r.val:
                res = False
            l = l.next
            r = r.next
        mid.next = reverse(tmp)
        return res
