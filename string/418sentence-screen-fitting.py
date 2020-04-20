from typing import List


class Solution:
    # check how many sentence fit each row
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ln = [len(s) for s in sentence]
        N = len(ln)
        length = sum(ln) + N

        res = 0
        index = 0
        for i in range(rows):
            remain_cols = cols
            while remain_cols > 0:
                # enough for the next word
                if ln[index] <= remain_cols:
                    remain_cols -= ln[index]
                    # add a space
                    if remain_cols > 0:
                        remain_cols -= 1
                    # +one word is filled
                    index += 1
                    # entire sentence is filled
                    if index == N:
                        # put next sentence
                        # divmod(x, y) == (x//y, x%y)
                        div, mod = divmod(remain_cols, length)
                        res += (div + 1)
                        remain_cols = mod
                        index = 0
                else:
                    break
        return res

    # dp
    def wordsTyping1(self, sentence: List[str], rows: int, cols: int) -> int:
        N = len(sentence)
        dp = [0] * N
        for i in range(N):
            w, l, num = i, 0, 0
            while l + len(sentence[w]) <= cols:
                num += 1
                l += len(sentence[w]) + 1
                w += 1
                if w == N:
                    w = 0
            dp[i] = num
        res = 0
        start = 0
        for i in range(rows):
            res += dp[start]
            start = (start + dp[start]) % N
        return res // N


sol = Solution()
print(sol.wordsTyping(["I", "had", "apple", "pie"], 4, 5))
print(sol.wordsTyping1(["I", "had", "apple", "pie"], 4, 5))
print(sol.wordsTyping(["a", "bcd", "e"], 3, 6))
print(sol.wordsTyping1(["a", "bcd", "e"], 3, 6))
