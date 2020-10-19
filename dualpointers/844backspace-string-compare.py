class Solution:
    # use stack to simulate: O(n+m), (n+m)
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s):
            stack = []
            for ch in s:
                # careful here
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return build(S) == build(T)

    # backword dual pointers: O(n+m), O(1)
    def backspaceCompare1(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS, skipT = 0, 0
        while i >= 0 or j >= 0:
            # move i and j to the next actual existing ch in S and T
            while i >= 0:
                if S[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    i -= 1
                    skipS -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    j -= 1
                    skipT -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                # one ends but another not
                # empty != nonempty
                return False
            i -= 1
            j -= 1
        return i == j


s = Solution()
print(s.backspaceCompare1("bxj##tw", "bxj###tw"))
