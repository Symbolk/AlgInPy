from typing import List
import collections


class Solution:
    # DFS: O(nc), O(nc)
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        f = [[0] * 26 for _ in range(n)]

        # since edge has no direction, use pre as parent
        # each node only has one pre
        def dfs(cur, pre):
            # convert label char to int
            f[cur][ord(labels[cur]) - ord('a')] = 1
            for nxt in g[cur]:
                if nxt != pre:
                    dfs(nxt, cur)
                    for i in range(26):
                        f[cur][i] += f[nxt][i]

        dfs(0, -1)
        return [f[i][ord(labels[i]) - ord('a')] for i in range(n)]

    # DFS by mark visited (parent will be visited before child)
    def countSubTrees1(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        res = [0] * n

        def dfs(cur):
            visited[cur] = True
            cnt = [0] * 26
            cnt[ord(labels[cur]) - ord('a')] += 1
            for nxt in g[cur]:
                if not visited[nxt]:
                    child = dfs(nxt)
                    for i in range(26):
                        cnt[i] += child[i]
            res[cur] = cnt[ord(labels[cur]) - ord('a')]
            return cnt

        dfs(0)
        return res

    def countSubTrees2(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        res = [0] * n

        def dfs(cur):
            visited[cur] = True
            cnt = collections.defaultdict(int)
            cnt[labels[cur]] = 1
            for nxt in g[cur]:
                if not visited[nxt]:
                    child = dfs(nxt)
                    for c in child:
                        cnt[c] += child[c]
            res[cur] = cnt[labels[cur]]
            return cnt

        dfs(0)
        return res


s = Solution()
print(s.countSubTrees2(25,
                       [[4, 0], [5, 4], [12, 5], [3, 12], [18, 3], [10, 18], [8, 5], [16, 8], [14, 16], [13, 16],
                        [9, 13], [22, 9], [2, 5], [6, 2], [1, 6], [11, 1], [15, 11], [20, 11], [7, 20], [19, 1],
                        [17, 19], [23, 19], [24, 2], [21, 24]],
                       "hcheiavadwjctaortvpsflssg"))
