from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
