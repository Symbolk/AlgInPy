# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n), O(1)
    # corner cases:
    #   head is None
    #   k > len(linkedlist)
    #   k = 0
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i, j = head, head
        for _ in range(k):
            i = i.next

        while i:
            i = i.next
            j = j.next

        return j