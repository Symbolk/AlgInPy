class Solution:
    # dfs coloring: O(N+E), O(N+E)
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        # or use array/defaultdict
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            for nxt in graph[node]:
                # 0^1=1 1^1=0
                if not dfs(nxt, c ^ 1):  # ^ XOR
                    return False
            return True
            # return all(dfs(nxt, c ^ 1) for nxt in graph[node])

        return all(dfs(node, 0) for node in range(N) if node not in color)

    # bfs
    def possibleBipartition1(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        stack = collections.deque()
        for i in range(1, N + 1):
            if i not in color:
                color[i] = 0
                stack.append((i, 0))
            while stack:
                u, c = stack.popleft()
                for v in graph[u]:
                    if v in color:
                        if color[v] == color[u]:
                            return False
                    else:
                        # 1-1=0, 1-0=1
                        # or use 1 and -1
                        color[v] = 1 - c
                        stack.append((v, 1 - c))

        return True
