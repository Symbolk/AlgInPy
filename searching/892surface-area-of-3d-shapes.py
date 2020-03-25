from typing import List


class Solution:
    # add: O(n^2), O(1)
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        move_i = [-1, 1, 0, 0]
        move_j = [0, 0, -1, 1]
        res = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 0:
                    for k in range(4):
                        n_i, n_j = i + move_i[k], j + move_j[k]
                        if 0 <= n_i < N and 0 <= n_j < N:
                            # res += max(grid[i][j] - grid[n_i][n_j], 0)
                            if grid[n_i][n_j] < grid[i][j]:
                                res += (grid[i][j] - grid[n_i][n_j])
                        else:
                            res += grid[i][j]
                    # top and bottom
                    res += 2
        return res

    def surfaceArea1(self, grid: List[List[int]]) -> int:
        N = len(grid)
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    for dx, dy in move:
                        n_i, n_j = i + dx, j + dy
                        if 0 <= n_i < N and 0 <= n_j < N:
                            res += max(grid[i][j] - grid[n_i][n_j], 0)
                        else:
                            res += grid[i][j]
                    # top and bottom
                    res += 2
        return res

    # minus:
    def surfaceArea2(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # overlapping faces
        faces = 0
        num = 0
        for i in range(N):
            for j in range(N):
                num += grid[i][j]
                if grid[i][j]:
                    faces += grid[i][j] - 1
                if i > 0:
                    faces += min(grid[i - 1][j], grid[i][j])
                if j > 0:
                    faces += min(grid[i][j - 1], grid[i][j])
        return 6 * num - 2 * faces


sol = Solution()
print(sol.surfaceArea([[2]]))
print(sol.surfaceArea([[1, 2], [3, 4]]))
print(sol.surfaceArea([[1, 0], [0, 2]]))
print(sol.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(sol.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
