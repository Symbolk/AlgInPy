# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # enumerate the next node of current: O(n), O(n)
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        seen = {head.val}
        # head cannot be changed
        pos = head
        while pos.next:
            cur = pos.next
            if cur.val in seen:
                # pos.next changed so it moves
                pos.next = pos.next.next
            else:
                seen.add(cur.val)
                pos = pos.next
        return head
