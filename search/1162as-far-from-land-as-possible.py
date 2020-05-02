from typing import List


class Solution:
    # multi-source BFS with deque: O(n^2), O(n^2)
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        N = len(grid)
        steps = -1
        q = deque([(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1])
        if len(q) == 0 or len(q) == N ** 2:
            return steps
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(q) > 0:
            for _ in range(len(q)):
                x, y = q.popleft()  # list.pop(0) is O(n), so use deque
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        grid[nx][ny] = -1
            steps += 1

        return steps

    # multi-source BFS with queue(array)
    def maxDistance1(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = [(i, j) for i in range(N) for j in range(N) if grid[i][j]]

        if not q or len(q) == N * N:
            return -1

        steps = -1  # depth of BFS
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            steps += 1
            seas = []  # seas to explore in the next level
            for x, y in q:  # for each land in the current level
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not grid[nx][ny]:
                        seas.append((nx, ny))
                        grid[nx][ny] = 1  # mark as visited
            q = seas
        return steps

    def maxDistance2(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = [(i, j) for i in range(N) for j in range(N) if grid[i][j]]

        if not q or len(q) == N * N:
            return -1

        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            num = len(q)
            for i in range(num):  # for each land in the current level
                x, y = q.pop(0)
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not grid[nx][ny]:
                        q.append((nx, ny))
                        grid[nx][ny] = grid[x][y] + 1
        return grid[x][y] - 1

    # Dijkstra
    def maxDistance3(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[float('inf')] * n for _ in range(n)]
        priority_queue = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isValid(x, y):
            if x < 0 or x >= n or y < 0 or y >= n: return False
            return True

        for i in range(n):
            for j in range(n):
                if grid[i][j]:  # ->island
                    d[i][j] = 0
                    heapq.heappush(priority_queue, [0, i, j])

        while priority_queue:
            step, x, y = heapq.heappop(priority_queue)
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if isValid(next_x, next_y) and d[next_x][next_y] > step + 1:
                    d[next_x][next_y] = step + 1
                    heapq.heappush(priority_queue, [step + 1, next_x, next_y])

        ans = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: ans = max(ans, d[i][j])

        return ans if ans != float('inf') else -1

    # SPFA
    def maxDistance4(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d, inQueue = [[float('inf')] * n for _ in range(n)], [[False] * n for _ in range(n)]
        queue = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isValid(x, y):
            if x < 0 or x >= n or y < 0 or y >= n: return False
            return True

        for i in range(n):
            for j in range(n):
                if grid[i][j]:  # ->island
                    d[i][j] = 0
                    queue.append([i, j])
                    inQueue[i][j] = True

        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if isValid(next_x, next_y) and d[next_x][next_y] > d[x][y] + 1:
                    d[next_x][next_y] = d[x][y] + 1
                    if not inQueue[next_x][next_y]:
                        queue.append([next_x, next_y])
                        inQueue[next_x][next_y] = True

        ans = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: ans = max(ans, d[i][j])

        return ans if ans != float('inf') else -1


sol = Solution()
print(sol.maxDistance2([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
print(sol.maxDistance2([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(sol.maxDistance2([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
