# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iteration with two pointers: O(n), O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            # revert
            tmp = cur.next
            cur.next = pre
            # move forward by 1 step
            pre = cur
            cur = tmp
        # return the new head node
        return pre

    def reverseList0(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    # recursion: O(n), O(n)
    def reverseList1(self, head: ListNode) -> ListNode:
        # base case/terminator
        if not head or not head.next:
            return head
        # cur is the last
        cur = self.reverseList1(head.next)
        head.next.next = head
        # to avoid loop
        head.next = None
        return cur
