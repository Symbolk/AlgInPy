from collections import defaultdict


class Solution:
    def solveSudoku(self, board):
        """
        Check if d can be placed in (x, y)
        :param board:
        :return:
        """

        def can_place(d, x, y):
            return not (d in rows[x] or d in cols[y] or d in boxes[box_index(x, y)])

        """
        Place the number in (x, y)
        """

        def place(d, x, y):
            rows[x][d] += 1
            cols[y][d] += 1
            boxes[box_index(x, y)][d] += 1
            board[x][y] = str(d)

        def remove(d, x, y):
            del rows[x][d]
            del cols[y][d]
            del boxes[box_index(x, y)][d]
            board[x][y] = '.'

        def place_next(x, y):
            if x == N - 1 and y == N - 1:
                nonlocal solved
                solved = True
            else:
                if y == N - 1:
                    backtrack(x + 1, 0)
                else:
                    backtrack(x, y + 1)

        def backtrack(x, y):
            if board[x][y] == '.':
                for d in range(1, 10):
                    if can_place(d, x, y):
                        place(d, x, y)
                        place_next(x, y)
                        if not solved:
                            remove(d, x, y)
            else:
                place_next(x, y)

        n = 3
        N = n * n
        box_index = lambda x, y: (x // n) * n + y // n

        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place(d, i, j)
        solved = False
        backtrack(0, 0)

    def solveSudoku2(self, board):
        n = 3
        N = n * n
        get_index = lambda x, y: (x // n) * n + y // n

        # available numbers in row/col/block
        row = [set(range(1, 10)) for _ in range(N)]
        col = [set(range(1, 10)) for _ in range(N)]
        block = [set(range(1, 10)) for _ in range(N)]
        empty = []

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    row[i].remove(d)
                    col[j].remove(d)
                    block[get_index(i, j)].remove(d)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):
                return True
            i, j = empty[iter]
            index = get_index(i, j)
            for d in row[i] & col[j] & block[index]:
                row[i].remove(d)
                col[j].remove(d)
                block[index].remove(d)
                board[i][j] = str(d)
                if backtrack(iter + 1):
                    return True
                row[i].add(d)
                col[j].add(d)
                block[index].add(d)
            return False

        backtrack()


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol = Solution()
# sol.solveSudoku(board)
sol.solveSudoku2(board)
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=' ')
    print()
