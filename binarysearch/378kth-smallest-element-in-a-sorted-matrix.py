import heapq


class Solution:
    # min heap with size n: O(klogn), O(k)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(N)]
        heapq.heapify(pq)

        for i in range(k - 1):
            # pop the min
            n, x, y = heapq.heappop(pq)
            if y != N - 1:
                # push the next in the same row with the min
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        # the kth popped is the kth smallest
        return heapq.heappop(pq)[0]

    # binary search: O(nlog(r-l)), O(1)
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)

        def check(mid):
            # from left-bottom corner
            i, j = N - 1, 0
            # num of element <= mid
            num = 0
            while i >= 0 and j < N:
                if matrix[i][j] <= mid:
                    num += (i + 1)
                    # move right
                    j += 1
                else:
                    # move up
                    i -= 1
            return num >= k

        # global min and max
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1

        return l
