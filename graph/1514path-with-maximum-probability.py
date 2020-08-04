import collections
from queue import PriorityQueue
import heapq
import math
from typing import List


class Solution:
    # bfs, dijistra
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # build adjacency matrix
        dic = collections.defaultdict(dict)
        for i, (s, t) in enumerate(edges):
            # s, t = e  # list unpack
            dic[s][t] = succProb[i]
            dic[t][s] = succProb[i]
        q = [(-1, start)]
        visited = {start}
        while q:
            prob, node = heapq.heappop(q)
            if node == end:
                return -prob
            visited.add(node)
            for next in dic[node]:
                if next not in visited:
                    heapq.heappush(q, (prob * dic[node][next], next))
        return 0


sol = Solution()
print(sol.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
