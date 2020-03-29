from typing import List


class Solution:
    # BFS: O(n^2), O(n^2)
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
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        grid[nx][ny] = -1
            steps += 1

        return steps


sol = Solution()
print(sol.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
print(sol.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(sol.maxDistance([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
