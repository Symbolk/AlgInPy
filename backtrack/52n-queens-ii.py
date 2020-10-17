class Solution:
    def solveNQueens(self, n: int) -> int:
        cols = set()
        # for main diagonals: i-j keeps
        # for vice diagonals: i+j keeps
        main = set()
        vice = set()

        def backtrack(row):
            if row == n:
                return 1
            else:
                count = 0
                # try every col in this row
                for i in range(n):
                    if i in cols or row - i in main or row + i in vice:
                        continue
                    # put
                    cols.add(i)
                    main.add(row - i)
                    vice.add(row + i)
                    count += backtrack(row + 1)
                    # revert
                    cols.remove(i)
                    main.remove(row - i)
                    vice.remove(row + i)
                return count

        return backtrack(0)
