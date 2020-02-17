class Solution:
    def toLowerCase(self, str: str) -> str:
        # return str.lower()
        # learn str operations
        ls = list(str)
        for s in ls:
            if ord(s) >= 65 and ord(s) <= 90:
                ls[ls.index(s)] = chr(ord(s) + 32)
        return "".join(ls)


if __name__ == "__main__":
    solution = Solution()
    print(solution.toLowerCase("JJJFfg"))
