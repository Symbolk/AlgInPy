# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # cache and sort: O(nlogn), O(n)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums = []
        while l1:
            nums.append(l1.val)
            l1 = l1.next
        while l2:
            nums.append(l2.val)
            l2 = l2.next
        head = cur = ListNode(None)
        for n in sorted(nums):
            cur.next = ListNode(n)
            cur = cur.next
        return head.next

    # iteration: compare and link O(n+m), O(1) (no need to create new ListNode)
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # extra
        cur.next = l1 if l1 else l2
        # if l1:
        #     cur.next = l1
        # if l2:
        #     cur.next = l2
        return head.next

    # recursion: O(n+m), O(n+m) (recursion stack depth)
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                # !trick here: swap l1 and l2, save min in l1, merge into l1
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1 or l2

    # recursion: O(n+m), O(n+m)
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists3(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists3(l1, l2.next)
                return l2
        else:
            return l1 or l2

