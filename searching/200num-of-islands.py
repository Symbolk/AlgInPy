from typing import List


# notice the type of the input: str instead of int!
class Solution:
    # sink/flood-fill/DFS/recursion
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        if not N:
            return 0
        M = len(grid[0])

        def sink(i, j):
            grid[i][j] = '0'
            for dx, dy in move:
                n_i, n_j = i + dx, j + dy
                if 0 <= n_i < N and 0 <= n_j < M and grid[n_i][n_j] == '1':
                    sink(n_i, n_j)

        res = 0
        move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    res += 1
                    sink(i, j)

        return res

    # BFS:
    def numIslands1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        N, M = len(grid), len(grid[0])
        res = 0
        move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        from collections import deque
        def bfs(i, j):
            q = deque()
            q.appendleft((i, j))
            grid[i][j] = '0'
            while q:
                i, j = q.pop()
                for dx, dy in move:
                    n_i, n_j = i + dx, j + dy
                    if 0 <= n_i < N and 0 <= n_j < M and grid[n_i][n_j] == '1':
                        grid[n_i][n_j] = '0'
                        q.appendleft((n_i, n_j))

        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1

        return res

    # union-find/disjoint sets
    def numIslands2(self, grid: List[List[str]]) -> int:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            # find root to shorten path
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        if not grid:
            return 0
        N, M = len(grid), len(grid[0])
        move = [(-1, 0), (0, -1)]  # 84ms
        # move = [(1, 0), (0, 1)] # 156ms
        # move = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 192ms

        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    for dx, dy in move:
                        n_i, n_j = i + dx, j + dy
                        if 0 <= n_i < N and 0 <= n_j < M and grid[n_i][n_j] == '1':
                            # index = i * #cols + j
                            union(n_i * M + n_j, i * M + j)

        res = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    res.add(find(i * M + j))
        return len(res)

    # union-find with rank (# 136ms because it's not worth the cost)
    def numIslands3(self, grid: List[List[str]]) -> int:
        parent = {}
        rank = {}

        def find(x):
            parent.setdefault(x, x)
            rank.setdefault(x, 0)
            # find root to shorten path
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # link the shallow tree into the depth tree
            x, y = find(x), find(y)
            if x != y:
                if rank[x] <= rank[y]:
                    parent[x] = y
                    rank[y] = max(rank[y], rank[x] + 1)
                else:
                    parent[y] = x
                    rank[x] + max(rank[x], rank[y] + 1)

        if not grid:
            return 0
        N, M = len(grid), len(grid[0])
        move = [(-1, 0), (0, -1)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    for dx, dy in move:
                        n_i, n_j = i + dx, j + dy
                        if 0 <= n_i < N and 0 <= n_j < M and grid[n_i][n_j] == '1':
                            # index = i * #cols + j
                            union(n_i * M + n_j, i * M + j)

        res = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '1':
                    res.add(find(i * M + j))
        return len(res)
