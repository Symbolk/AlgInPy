from typing import List
import collections


class Solution:
    # DFS: O(n^2), O(n)
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dic = collections.defaultdict(set)
        N = len(graph)
        for u, vs in enumerate(graph):
            for v in vs:
                dic[u].add(v)
                dic[v].add(u)
        # color node n with c
        color = [0] * N

        def dfs(u, c):
            color[u] = c
            for v in dic[u]:
                if color[v] == c:
                    return False
                if color[v] == 0 and not dfs(v, -c):
                    return False
            return True

        for i in range(N):
            # each node should only be colored once
            if color[i] == 0 and not dfs(i, 1):
                return False

        return True

    # quicker DFS: O(n+m), O(n)
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        color = [0] * N

        def dfs(u, c):
            color[u] = c
            for v in graph[u]:
                if color[v] == 0 and not dfs(v, -c):
                    return False
                elif color[v] == c:
                    return False
            return True

        for i in range(N):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True

    # BFS: O(n+m), O(n)
    def isBipartite2(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        color = [0] * N
        for i in range(N):
            if color[i] == 0:
                color[i] = 1
                q = collections.deque()
                q.append((i, 1))
                while q:
                    u, c = q.popleft()
                    for v in graph[u]:
                        if color[v] == 0:
                            color[v] = -c
                            q.append((v, -c))
                        elif color[v] == c:
                            return False
        return True

    # UFS: O(n+m), O(n)
    def isBipartite3(self, graph: List[List[int]]) -> bool:
        uf = UnionFind(len(graph))
        for u, vs in enumerate(graph):
            for v in vs:
                if uf.is_connected(u, v):
                    return False
                uf.union(vs[0], v)
        return True


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def find1(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


sol = Solution()
print(sol.isBipartite3([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(sol.isBipartite3([[1], [0, 3], [3], [1, 2]]))
print(sol.isBipartite3([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
