class Solution:
    # BFS with deque: O(mn), O(mn)
    def movingCount(self, m: int, n: int, k: int) -> int:
        from functools import reduce
        # def digitSum(a):
        #     res = 0
        #     for i in str(a):
        #         res += int(i)
        #     return res
        def digitSum(a):
            return int(reduce(lambda x, y: int(x) + int(y), str(a)))

        from collections import deque
        q = deque()
        q.append((0, 0))
        reachable = set()

        # right or down
        move = [(1, 0), (0, 1)]

        while q:
            x, y = q.popleft()
            if (x, y) not in reachable and 0 <= x < m and 0 <= y < n and digitSum(x) + digitSum(y) <= k:
                reachable.add((x, y))
                # to next states
                for dx, dy in move:
                    q.append((x + dx, y + dy))

        return len(reachable)

    # BFS with Queue: O(mn), O(mn)
    def movingCount1(self, m: int, n: int, k: int) -> int:
        def digitSum(a):
            ans = 0
            while a:
                ans += a % 10
                a //= 10
            return ans

        from queue import Queue
        q = Queue()
        q.put((0, 0))
        reachable = set()

        # right or down
        move = [(1, 0), (0, 1)]

        while not q.empty():
            x, y = q.get()
            if (x, y) not in reachable and 0 <= x < m and 0 <= y < n and digitSum(x) + digitSum(y) <= k:
                reachable.add((x, y))
                # to next states
                for dx, dy in move:
                    q.put((x + dx, y + dy))

        return len(reachable)

    # inference/dp: vis[i][j]=vis[i−1][j] or vis[i][j−1]
    def movingCount2(self, m: int, n: int, k: int) -> int:
        from functools import reduce
        def digitSum(a):
            return int(reduce(lambda x, y: int(x) + int(y), str(a)))

        vis = set()
        vis.add((0, 0))
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitSum(i) + digitSum(j) <= k:
                    vis.add((i, j))

        return len(vis)


sol = Solution()
print(sol.movingCount(2, 3, 1))
print(sol.movingCount(3, 1, 0))
print(sol.movingCount1(16, 8, 4))
print(sol.movingCount2(16, 8, 4))
