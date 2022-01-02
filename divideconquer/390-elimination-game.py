class Solution:
    def lastRemaining(self, n: int) -> int:
        a1 = 1
        k, cnt, s = 0, n, 1
        while cnt > 1:
            if k % 2:
                if cnt % 2:
                    a1 += s
            else:
                a1 += s
            k += 1
            s <<= 1
            cnt >>= 1
        return a1
