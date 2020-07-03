# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # iteration: O(nlogn), O(logn)
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # note the diff with from array
        def findMid(head, tail):
            s = f = head
            while f != tail and f.next != tail:
                f = f.next.next
                s = s.next
            return s

        def bst(head, tail):
            if head == tail:
                return None
            mid = findMid(head, tail)
            root = TreeNode(mid.val)
            root.left = bst(head, mid)
            root.right = bst(mid.next, tail)
            return root

        return bst(head, None)

    # O(n), O(logn)
    def __init__(self):
        self.head = None

    def bst(self, l, r):
        if l > r:
            return None
        m = (l + r) // 2
        left = self.bst(l, m - 1)
        root = TreeNode(self.head.val)
        self.head = self.head.next
        root.left = left
        right = self.bst(m + 1, r)
        root.right = right
        return root

    def sortedListToBST1(self, head: ListNode) -> TreeNode:
        self.head = head
        N = 0
        while head:
            N += 1
            head = head.next

        return self.bst(0, N - 1)
