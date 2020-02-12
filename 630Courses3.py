from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda l: l[1])
        q = []
        d = 0 # date
        for c in courses:
            if d + c[0] <= c[1]:
                d += c[0]
                # use - to simulate max heap
                heapq.heappush(q, -c[0])
            elif q and -q[0] > c[0]:
                # heapq.heappop(q) < 0, remove the longest one
                d += c[0] + heapq.heappop(q)
                heapq.heappush(q, -c[0])
        return len(q)


sol = Solution()
print(sol.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
