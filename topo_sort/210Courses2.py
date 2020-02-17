from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        queue = [k for k in range(numCourses) if not indegrees[k]]
        # queue = []
        # for i in range(numCourses):
        #     if indegrees[i] == 0:
        #         queue.append(i)

        res = []
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)

        return res if len(res) == numCourses else []

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        # as a stack, reversed order
        res = []
        flag = True
        state = [0 for _ in range(numCourses)]

        def dfs(node):
            nonlocal flag
            if not flag:
                return
            state[node] = 1
            for cur in adjacency[node]:
                if state[cur] == 0:
                    dfs(cur)
                elif state[cur] == 1:
                    flag = False
            state[node] = 2
            res.append(node)

        for node in range(numCourses):
            if state[node] == 0:
                dfs(node)

        return res[::-1] if flag else []


sol = Solution()
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(sol.findOrder2(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
