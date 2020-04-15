# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @lc code=start
# Definition for singly-linked list.
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class Solution:
    # return the result linked list without head dummy node
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if isinstance(l1, list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)

        carry = 0
        # head is always the head
        head = ListNode(-1)
        # tail is used to append
        tail = head
        while l1 or l2 or carry != 0:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            cur = a + b + carry
            carry = cur // 10
            cur = cur % 10
            cur_node = ListNode(cur)
            # !append
            tail.next = cur_node
            tail = cur_node

        return head.next


# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.addTwoNumbers([1, 3], [2, 1, 3]))
