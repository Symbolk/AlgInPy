class Solution:
    # math: Bézout's identity O(log(min(x, y))
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0

    # every action change x/y for the sum of the water, so find (a, b) to make ax+by=z
    # Bezout's identity: (a,b) exists iff z % gcd(x,y)==0
    def canMeasureWater0(self, x: int, y: int, z: int) -> bool:
        return x + y >= z and (z == 0 or y and z % math.gcd(x, y) == 0)

    # DFS: O(xy), O(xy) (max reachable states num: (x+1)(y+1))
    def canMeasureWater1(self, x: int, y: int, z: int) -> bool:
        # or deque and pop()
        stack = [(0, 0)]
        visited = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in visited:
                continue
            visited.add((remain_x, remain_y))
            stack.append((x, remain_y))
            stack.append((remain_x, y))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False

    # BFS: O(xy),  O(xy)
    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
        if z < 0 or x + y < z:
            return False
        from collections import deque
        q = deque([(0, 0)])
        visited = {(0, 0)}

        while q:
            a, b = q.popleft()
            if a == z or b == z or a + b == z:
                return True
            next_states = [
                (0, b), (a, 0),  # drop a or b
                (x, b), (a, y),  # fill x or y
                (0, a + b) if a + b < y else (a + b - y, y),  # a -> b
                (a + b, 0) if a + b < x else (x, a + b - x)  # b -> a
            ]
            for state in next_states:
                if state not in visited:
                    q.append(state)
                    visited.add(state)
        return False

    # BFS: O(xy),  O(xy)
    def canMeasureWater3(self, x: int, y: int, z: int) -> bool:
        if z < 0 or x + y < z:
            return False
        from collections import deque
        q = deque([0])
        visited = {0}

        while q:
            total = q.popleft()
            if total == z:
                return True
            next_states = [
                total + x if total + x < x + y else x + y,
                total + y if total + y < x + y else x + y,
                total - x if total - x > 0 else 0,
                total - y if total - y > 0 else 0
            ]
            for state in next_states:
                if state not in visited:
                    q.append(state)
                    visited.add(state)
        return False


sol = Solution()
print(sol.canMeasureWater3(3, 5, 4))
