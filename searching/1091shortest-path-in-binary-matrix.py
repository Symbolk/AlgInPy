from typing import List
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # if priority bigger = better, should use -priority
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return len(self._queue) == 0


class Solution:
    def shortestPathBinaryMatrix0(self, grid: List[List[int]]) -> int:
        # distance to the dest
        N = len(grid)
        if not grid or grid[0][0] == 1 or grid[N - 1][N - 1] == 1:
            return -1
        elif N <= 2:
            return N

        def distance(x, y):
            return max(abs(N - 1 - x), abs(N - 1 - y))

        pq = []
        visited = set()
        heapq.heappush(pq, (0, (0, 0, 1)))
        move = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        while pq:
            # get the one with min distance + step
            _, (i, j, step) = heapq.heappop(pq)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for dx, dy in move:
                next_i, next_j = i + dx, j + dy
                if next_i == N - 1 and next_j == N - 1:
                    return step + 1
                # !here next_i can be N-1 or next_j can be N-1, so cannot use < N - 1
                if 0 <= next_i < N and 0 <= next_j < N and grid[next_i][next_j] == 0:
                    heapq.heappush(pq, (step + distance(next_i, next_j), (next_i, next_j, step + 1)))
        return -1

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
            # queue pop(0): O(n), use deque.popleft(): O(1) next time
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

print(sol.shortestPathBinaryMatrix0([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
