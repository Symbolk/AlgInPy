from typing import List


class Solution:
    # merge k sorted lists: O(nklogk), O(k)
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        from queue import PriorityQueue
        q = PriorityQueue()
        N = len(nums)
        INF = 10 ** 9
        maxv = -INF
        start, end = -INF, INF

        for i in range(N):
            # PQ sort elements by order
            # put the head into PQ
            q.put((nums[i][0], i, 0))
            maxv = max(maxv, nums[i][0])

        while q.qsize() == N:
            v, i, j = q.get()
            if maxv - v < end - start:
                start, end = v, maxv
            if j + 1 < len(nums[i]):
                nv = nums[i][j + 1]
                q.put((nv, i, j + 1))
                maxv = max(maxv, nv)
        return [start, end]

    # heap to simulate PQ
    def smallestRange1(self, nums: List[List[int]]) -> List[int]:
        import heapq
        N = len(nums)
        INF = 10 ** 9
        start, end = -INF, INF
        maxv = -INF
        q = []
        for i in range(N):
            q.append((nums[i][0], i, 0))
            maxv = max(maxv, nums[i][0])
        heapq.heapify(q)
        while True:
            v, i, j = heapq.heappop(q)
            if maxv - v < end - start:
                start, end = v, maxv
            if j + 1 >= len(nums[i]):
                break
            else:
                heapq.heappush(q, (nums[i][j + 1], i, j + 1))
                maxv = max(maxv, nums[i][j + 1])

        return [start, end]


s = Solution()
print(s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(s.smallestRange1([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
