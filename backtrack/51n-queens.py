from typing import List


class Solution:
    # O(n!), O(n)
    # bitwise to check conflicts/attacks
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return
        self.count = 0
        self.res = []
        self.dfs(n, 0, 0, 0, 0, [])
        return self.res

    def dfs(self, n, row, cols, pie, na, row_pos):
        if row >= n:
            self.count += 1
            self.res.append(["." * p + "Q" * (n - p - 1) for p in row_pos])
            return
        # 0: has_queen or attack
        # 1: no_queen and not_attack
        bits = (~(cols | pie | na)) & ((1 << n) - 1)

        while bits:
            p = bits & -bits  # get the col of the last 1
            # pie: attack the down and left col
            # na: attack the down and right col
            self.dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1, row_pos + [p])
            bits &= (bits - 1)  # set the last 1 (at p) to 0

    def solveNQueens1(self, n: int) -> List[List[str]]:
        res = list()
        # queens index for each row
        pos = [-1] * n
        row = ['.'] * n
        # use sets to remember attacks
        cols = set()
        main = set()
        vice = set()

        def backtrack(r):
            if r == n:
                res.append(generate())
            else:
                # for each col in this row
                for i in range(n):
                    if i in cols or r - i in main or r + i in vice:
                        continue
                    else:
                        pos[r] = i
                        cols.add(i)
                        main.add(r - i)
                        vice.add(r + i)
                        backtrack(r + 1)
                        cols.remove(i)
                        main.remove(r - i)
                        vice.remove(r + i)

        def generate():
            board = list()
            for i in range(n):
                row[pos[i]] = 'Q'
                board.append(''.join(row))
                row[pos[i]] = '.'
            return board

        backtrack(0)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))
