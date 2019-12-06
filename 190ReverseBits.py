class Solution:
    def reverseBits(self, n: int) -> int:
        res = bin(n)[2:]
        # 返回指定长度的字符串，原字符串右对齐，前面填充0
        res = res.zfill(32)
        # reverse the list
        res = res[::-1]
        return int(res, base=2)

if __name__=="__main__":
    solution = Solution()
    print(solution.reverseBits(5))