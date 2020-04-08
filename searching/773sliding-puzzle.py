from typing import List


class Solution:
    # min #steps-->BFS: search for the target state in the solution space
    # O(R∗C∗(R∗C)!)
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        # to 1-d
        board = board[0] + board[1]
        # next state of block0 at each pos (hard code)
        move = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        q = deque()
        # convert list (mutable) to a hashable (immutable) tuple, as the node in the solution space
        q.append([tuple(board), board.index(0), 0])
        visited = set()
        while q:
            state, pos, step = q.popleft()
            if state == (1, 2, 3, 4, 5, 0):
                return step
            for next_pos in move[pos]:
                # swap to get the next state
                _state = list(state)
                _state[next_pos], _state[pos] = _state[pos], _state[next_pos]
                _state = tuple(_state)
                if _state not in visited:
                    q.append((_state, next_pos, step + 1))
            visited.add(state)
        return -1

    # BFS (not hard code)
    def slidingPuzzle1(self, board: List[List[int]]) -> int:
        import itertools
        from collections import deque
        R, C = len(board), len(board[0])

        # to 1-d and hashable tuple
        start = tuple(itertools.chain(*board))
        q = deque([(start, start.index(0), 0)])
        visited = {start}
        target = tuple([*range(1, R * C)] + [0])
        # target = tuple([*range(1, R * C), [0]])

        # left, right, up, down
        move = (-1, 1, -C, C)

        while q:
            state, pos, step = q.popleft()
            if state == target:
                return step
            for d in move:
                _pos = pos + d
                # check if valid
                if abs(_pos // C - pos // C) + abs(_pos % C - pos % C) != 1:
                    continue
                if 0 <= _pos < R * C:
                    _state = list(state)
                    _state[_pos], _state[pos] = _state[pos], _state[_pos]
                    _state = tuple(_state)
                    if _state not in visited:
                        visited.add(_state)
                        q.append((_state, _pos, step + 1))
        return -1

    # heuristic search (A*): use list and heappush()/heappop() to simulate a priority queue
    def slidingPuzzle2(self, board: List[List[int]]) -> int:
        import itertools
        # default: min heap
        import heapq
        R, C = len(board), len(board[0])
        # chain iterators into a bigger iterator
        start = tuple(itertools.chain(*board))
        # python unpacking with *
        target = tuple([*range(1, R * C)] + [0])
        wrong = tuple([*range(1, R * C - 2)] + [R * C - 1, R * C - 2, 0])
        # heuristic distance, depth (step), state, pos of block0
        pq = [(0, 0, start, start.index(0))]
        # a dict of state:heuristic distance to expected state
        cost = {start: 0}
        # expected state: a dict of index:pos, e.g., 1: (0, 0)
        expected = {(C * r + c + 1) % (R * C): (r, c) for r in range(R) for c in range(C)}

        def fun(board):
            ans = 0
            for r in range(R):
                for c in range(C):
                    val = board[C * r + c]
                    # ! heuristic cost must be <= real cost
                    # if other blocks are correct, naturally 0 is correct
                    if val == 0:
                        continue
                    er, ec = expected[val]
                    # Manhattan Distance
                    ans += abs(r - er) + abs(c - ec)
            return ans

        while pq:
            distance, depth, state, pos = heapq.heappop(pq)
            if state == target:
                return depth
            # early stop at [1, 2, 3, 5, 4, 0] (a state that can never be corrected)
            if state == wrong:
                return -1
            if distance > cost[state]:
                continue

            for d in (-1, 1, -C, C):
                _pos = pos + d
                # check if the next_pos and the pos in the same line/column
                if abs(pos // C - _pos // C) + abs(pos % C - _pos % C) != 1:
                    continue
                if 0 <= _pos < R * C:
                    # tuple is immutable, so convert to list, swap, and back to tuple
                    _state = list(state)
                    _state[pos], _state[_pos] = _state[_pos], _state[pos]
                    _state = tuple(_state)
                    # cost = step that already taken + distance to the expected/target state
                    _cost = depth + 1 + fun(_state)
                    # get or default +inf
                    if _cost < cost.get(_state, float('inf')):
                        cost[_state] = _cost
                        heapq.heappush(pq, (_cost, depth + 1, _state, _pos))
        return -1


sol = Solution()
print(sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
print(sol.slidingPuzzle1([[4, 1, 2], [5, 0, 3]]))
print(sol.slidingPuzzle2([[4, 1, 2], [5, 0, 3]]))
