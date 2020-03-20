from typing import List
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0


class Solution:
    def shortestPathBinaryMatrix0(self, grid: List[List[int]]) -> int:
        def manDis(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        N = len(grid)
        if not grid or grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        elif N <= 2:
            return N
        pq = []
        min_step = N * N
        heapq.heappush(pq, (manDis(0, 0, N - 1, N - 1), (0, 0, 1)))
        move = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        while pq:
            dis, (i, j, step) = heapq.heappop(pq)
            for dx, dy in move:
                nextI, nextJ = i + dx, j + dy
                if nextI == N - 1 and nextJ == N - 1:
                    min_step = min(step + 1, min_step)
                if 0 <= nextI < N - 1 and 0 <= nextJ < N - 1 and grid[nextI][nextJ] == 0:
                    heapq.heappush(pq, (manDis(nextI, nextJ, N - 1, N - 1), (nextI, nextJ, step + 1)))
                    grid[nextI][nextJ] = 1
        return min_step

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # corner cases
        if not grid or grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        elif N <= 2:
            return N

        # BFS
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        move = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        while queue:
            i, j, step = queue.pop(0)
            for dx, dy in move:
                nextI, nextJ = i + dx, j + dy
                if nextI == N - 1 and nextJ == N - 1:
                    return step + 1
                if 0 <= nextI < N and 0 <= nextJ < N and grid[nextI][nextJ] == 0:
                    queue.append((nextI, nextJ, step + 1))
                    grid[nextI][nextJ] = 1
        return -1

    # more general
    def shortestPathBinaryMatrix1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # n * m
        visited = [[0] * m for _ in range(n)]
        if n == 1 and m == 1:
            return 1
        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        queue = [(0, 0)]
        visited[0][0] = 1
        step = 1
        temp_list = []
        while len(queue):
            cur_x, cur_y = queue.pop()
            step = visited[cur_x][cur_y]
            step += 1
            for i in range(8):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if next_x == n - 1 and next_y == m - 1:
                    return step
                if 0 <= next_x <= n - 1 and 0 <= next_y <= m - 1 and grid[next_x][next_y] == 0 and visited[next_x][
                    next_y] == 0:
                    temp_list.append((next_x, next_y))
                    visited[next_x][next_y] = step
                else:
                    continue
            if len(queue) == 0:
                queue = temp_list.copy()
                temp_list = []

        return -1


sol = Solution()
# print(sol.shortestPathBinaryMatrix0(
#     [[0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]]))
# print(sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(sol.shortestPathBinaryMatrix0(
    [[0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0]]))
