# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n), O(n)
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            # increment and then compare&relink
            i += 1
            if i == j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        # else: Error - Found cycle in the ListNode
        nodes[i].next = None

    # O(n), O(n)
    def reorderList0(self, head: ListNode) -> None:
        if not head:
            return None
        stack = []
        cur = head
        while cur.next:
            stack.append((cur, cur.next))
            cur = cur.next
        cur = head
        while cur.next and cur.next.next:
            # get one from the end of the list
            p, q = stack.pop()
            q.next = cur.next
            cur.next = q
            p.next = None
            cur = cur.next.next

    # really a good test for linkedlist
    # break the list, reverse the latter middle, merge two list
    # O(n), O(1)
    def reorderList1(self, head: ListNode) -> None:
        if not head:
            return None

        def findMid(node):
            slow = fast = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(node):
            pre, cur = None, node
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                # cur.next, pre, cur = pre, cur, cur.next
            return pre

        def merge(node1, node2):
            while node1 and node2:
                tmp1, tmp2 = node1.next, node2.next
                node1.next = node2
                node1 = tmp1
                node2.next = node1
                node2 = tmp2

        mid = findMid(head)
        l1, l2 = head, mid.next
        # break the list or there will be cycle
        mid.next = None
        l2 = reverse(l2)
        merge(l1, l2)
