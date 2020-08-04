from typing import List


class Solution:
    # topo sort: O(m+n), O(m+n)

    # BFS: forward, quicker with defaultdict and deque!
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        inds = [0] * numCourses
        for cur, pre in prerequisites:
            # save outgoing edges (pre -> cur)
            adj[pre].append(cur)
            # save indegree
            inds[cur] += 1

        q = collections.deque()
        # q = collections.deque([u for u in range(numCourses) if not inds[u]])
        for i in range(numCourses):
            if inds[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            numCourses -= 1
            # remove all outgoing edges from pre
            for nxt in adj[cur]:
                inds[nxt] -= 1
                if inds[nxt] == 0:
                    q.append(nxt)
        return (numCourses == 0)

    # DFS: backward, quicker with early stop
    def canFinish0(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        visited = [0] * numCourses

        def dfs(i):
            # has visited in the current dfs, found loop
            if visited[i] == 1:
                return False
            # has visited in other dfs, no need
            if visited[i] == -1:
                return True
            visited[i] = 1
            for j in adj[i]:
                if not dfs(j):
                    return False
            visited[i] = -1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    # @deprecated
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)  # pre->cur
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        # BFS toposort
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            # early stop
            if flags[i] == -1:
                return True
            # found loop
            if flags[i] == 1:
                return False
            # visited in current dfs
            flags[i] = 1
            for j in adjacency[i]:
                # j false
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True


sol = Solution()
print(sol.canFinish(2, [[1, 0], [0, 1]]))
print(sol.canFinish2(2, [[1, 0], [0, 1]]))
