# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Floyd: O(n), O(1)
    def detectCycle(self, head: ListNode) -> ListNode:
        i = j = head
        loop = False
        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                loop = True
                break
        if loop:
            i = head
            while i != j:
                i = i.next
                j = j.next
            return i
        return None
