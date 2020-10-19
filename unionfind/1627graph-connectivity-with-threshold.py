class Solution:
    # reverse thinking/tabling
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = [x for x in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(parent[y])

        for i in range(threshold + 1, n + 1):
            for j in range(i * 2, n + 1, i):
                union(i, j)

        return [find(x) == find(y) for x, y in queries]
