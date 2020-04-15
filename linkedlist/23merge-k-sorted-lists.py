# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# override the comparator of class
# def __lt__(self, other):
#     return self.val < other.val

class Solution:
    # speed increasing

    # priority queue to get the min node every time: O(nlogk), O(n) (k=#linkedlists)
    def mergeKLists0(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        head = cur = ListNode(None)
        q = PriorityQueue()
        # in python3, defined type cannot be compared, so we need an incremental index
        i = 0
        for l in lists:
            if l:
                q.put((l.val, i, l))
                i += 1

        while not q.empty():
            val, _, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, i, node))
                i += 1

        return head.next

    # brutal force: O(nlogn), O(n) (n=total numbers)
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
        head = ListNode(0)
        cur = head
        for n in sorted(nums):
            cur.next = ListNode(n)
            cur = cur.next

        return head.next

    # min heap to simulate priority queue, to avoid using k pointers to get the min
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        import heapq
        head = cur = ListNode(None)

        heap = []
        for i in range(len(lists)):
            # lists[i] is a ListNode in the ith linkedlist
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next

    def merge2Lists(self, l1, l2):
        head = cur = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next

    # divide and conquer/merge: O(nlogk), O(1)
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        K = len(lists)
        if K == 0:
            return lists
        interval = 1
        while interval < K:
            for i in range(0, K - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]
