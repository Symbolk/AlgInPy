class Solution:
    def reverseBits(self, n: int) -> int:
        res = bin(n)[2:]
        res = res.zfill(32)
        res = res[::-1]
        return int(res, base=2)


if __name__=="__main__":
    solution = Solution()
    solution.reverseBits(5)